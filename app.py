from concurrent.futures import thread
from flask import Flask, request, jsonify
from instagram_analytics import *
from threading import Thread
from helper_functions import *

app = Flask(__name__)


@app.route("/", methods = ["GET"])
def getAllDetails():
    
    conn = db_connection()
    cursor = conn.cursor()

    if request.method == "GET":
        cursor = conn.execute("SELECT * FROM app_user")
        data = [
            dict(id=row[0], user_id = row[3], instagram_account_id = row[4])
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
            params = getCreds()
            token_json = getAccessToken(params, code)
            print(token_json)
            access_token = token_json['access_token']
            print('access_token : ', access_token)
        except:
            print('access_token failed')
            access_token = 'Placeholder'
        
        try:
            life_access_token_json = getLifetimeToken(params, access_token)
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
        result = cursor.execute(sql, (code, access_token, user_id, instagram_account_id))
        print(result)
        conn.commit()
        conn.close()

        data = dict()
        data['code'] = code
        data['access_token'] = access_token
        data['user_id'] = user_id
        data['instagram_account_id'] = instagram_account_id

    return {"status": "success", "data": str(data)}         


@app.route("/bulk_update/<id>",  methods = ["GET"])
def bulkUpdate(id):
    thread = Thread(target=bulkUpdate_helper, args=(id,))
    thread.daemon = True
    thread.start()
    return jsonify({'thread_name': str(thread.name),
                    'started': True})


@app.route("/all_user_details/<id>",  methods = ["GET"])
def allUserDetails(id):
    data = getAllData_helper(id)
    return jsonify(data)


@app.route("/manual_upload", methods = ['POST'])
def manualUpload():
    code = request.args['code']
    access_token = request.args['access_token']
    user_id = request.args['user_id']
    instagram_account_id = request.args['instagram_account_id']
    
    conn = db_connection()
    cursor = conn.cursor()

    sql = '''INSERT INTO app_user (code, access_token, user_id, instagram_account_id) VALUES (?,?,?,?);'''
    print(sql)
    result = cursor.execute(sql, (code, access_token, user_id, instagram_account_id))
    print(result)
    conn.commit()
    conn.close()

    data = dict()
    data['code'] = code
    data['access_token'] = access_token
    data['user_id'] = user_id
    data['instagram_account_id'] = instagram_account_id

    return {"status": "success", "data": str(data)}    

########################
#### MAIN FUNCTION #####
########################

if __name__ == "__main__":
  app.run(host='0.0.0.0', port=8080, debug=True) 
