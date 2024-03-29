import atexit
from flask import Flask, request, jsonify
from instagram_analytics import *
from threading import Thread
from helper_functions import *
from apscheduler.schedulers.background import BackgroundScheduler

app = Flask(__name__)


@app.route("/", methods = ["GET"])
def getAllDetails():
    
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM app_user")
        data = [
            dict(id=row[0], client_id = row[1], user_id = row[5], instagram_account_id = row[6])
            for row in cursor.fetchall()
        ]
        
        conn.close()

        if data is not None:
            return jsonify(data)

        return {"status": "ok"}


# @app.route("/<id>", methods = ["GET"])
# def getUserData(id):
    
#     if not id:
#         return {"Error": "Send user id"}

#     conn = db_connection()
#     cursor = conn.cursor()
#     sql = '''SELECT %s FROM app_user WHERE %s = ?;'''
#     result = cursor.execute(sql % ('data','id',), (id,))
#     data = result.fetchone()[0]
#     conn.close()
    
#     return jsonify(data)


@app.route("/callback_token")
def callback_token():
    
    print('callback_token running...')
    print("request.args : ", request.args)
    
    if request.args['code'] is not None:
        
        try:
            print("request.args['code'] :", request.args['code'])
            code = request.args['code']
            print('code : ', code)
            client_secret = request.args['client_secret']
            client_id = request.args['client_id']
            params = getCreds()
            token_json = getAccessToken(params, client_id, client_secret, code)
            print(token_json)
            access_token = token_json['access_token']
            print('access_token : ', access_token)
        except:
            print('access_token failed')
            access_token = 'Placeholder'
        
        try:
            life_access_token_json = getLifetimeToken(params, client_id, client_secret, access_token)
            print('life_access_token_json : ', life_access_token_json)
            access_token = life_access_token_json['access_token']
            print('life_access_token : ', access_token)
        except:
            print('life_access_token failed')
            access_token = 'Placeholder'
        
        try:
            debug_json = getDebugToken(params, access_token)
            print('debug_json : ', debug_json)
            user_id = debug_json['data']['user_id']
            print('user_id : ', user_id)
        except:
            print('user_id failed')
            user_id = 'Placeholder'
        
        try:
            instagram_account_id = 'Placeholder'
            for elem in debug_json['granular_scopes']:
                if elem['scope'] == 'instagram_manage_insights':
                    instagram_account_id = elem['target_ids'][0]
            print('instagram_account_id : ', instagram_account_id)
        except:
            print('instagram_account_id failed')
            instagram_account_id = 'Placeholder'

        ## UPDATE DB
        conn = db_connection()
        cursor = conn.cursor()
        sql = '''INSERT INTO app_user (code, access_token, user_id, instagram_account_id) VALUES (?,?,?,?);'''
        print(sql)
        result = cursor.execute(sql, (client_id, client_secret, code, access_token, user_id, instagram_account_id))
        print(result)
        conn.commit()
        conn.close()

        data = {}
        data['client_id'] = client_id
        data['client_secret'] = client_secret
        data['code'] = code
        data['access_token'] = access_token
        data['user_id'] = user_id
        data['instagram_account_id'] = instagram_account_id

    return {"status": "success", "data": data}         


# @app.route("/bulk_update/<id>",  methods = ["GET"])
# def bulkUpdate(id):
#     thread = Thread(target=bulkUpdate_helper, args=(id,))
#     thread.daemon = True
#     thread.start()
#     return jsonify({'thread_name': str(thread.name),
#                     'started': True})


@app.route("/bulk_update_ig_id/<instagram_account_id>",  methods = ["GET"])
def bulkUpdate_ig_id(instagram_account_id):
    thread = Thread(target=bulk_upload_use_IG_Account_ID, args=(instagram_account_id,))
    thread.daemon = True
    thread.start()
    return jsonify({'thread_name': str(thread.name),
                    'started': True})


# @app.route("/all_user_details/<id>",  methods = ["GET"])
# def allUserDetails(id):
#     data = getAllData_helper(id)
#     return jsonify(data)


@app.route("/all_user_details_ig_id/<instagram_account_id>",  methods = ["GET"])
def allUserDetails_ig_id(instagram_account_id):
    data = getAllData_helper_ig_id(instagram_account_id)
    return jsonify(data)


@app.route("/manual_upload", methods = ['POST'])
def manualUpload():
    code = request.args['code']
    access_token = request.args['access_token']
    user_id = request.args['user_id']
    instagram_account_id = request.args['instagram_account_id']
    client_id = request.args['client_id']
    client_secret = request.args['client_secret']
    
    conn = db_connection()
    cursor = conn.cursor()

    sql = '''INSERT INTO app_user (client_id, client_secret, code, access_token, user_id, instagram_account_id) VALUES (?,?,?,?,?,?);'''
    # print(sql)
    result = cursor.execute(sql, (client_id, client_secret, code, access_token, user_id, instagram_account_id))
    # print(result)

    conn.commit()
    conn.close()

    data = {}
    data['client_id'] = client_id
    data['client_secret'] = client_secret    
    data['code'] = code
    data['access_token'] = access_token
    data['user_id'] = user_id
    data['instagram_account_id'] = instagram_account_id

    return {"status": "success", "data": data}    

# POST DATA TO AIRTABLE

@app.route("/post_to_airtable/<instagram_account_id>",  methods = ["GET"])
def post_to_airtable(instagram_account_id):
    url = 'https://hooks.airtable.com/workflows/v1/genericWebhook/appWbwpITbvT6NMYv/wflJnWkQ8pk0S81W3/wtrPyrotY4lOTOwEb'
    data = getAllData_helper_ig_id(instagram_account_id)

    try:
        data2 = data['media_insights']
        requests_session = requests.session()
        requests_session.headers.update({'Content-Type': 'application/json'})
        requests_session.headers.update({'charset':'utf-8'})
        requests_session.post(url=url, data={'data': data2})
    except Exception as e:
        print(e)
    
    return jsonify(data)


########################
#### MAIN FUNCTION #####
########################


scheduler = BackgroundScheduler()

scheduler.add_job(
    lambda: post_to_zapier(),
    "interval",
    minutes = 2,
    id='my_job_id'
)


scheduler.start()

atexit.register(lambda: scheduler.shutdown())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True) 
