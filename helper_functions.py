from logging import exception
from instagram_analytics import *
import sqlite3
import json


# ALL HELPER FUNCTIONS


def db_connection():
    conn = None
    
    try:
        conn = sqlite3.connect("ig_data.sqlite")
    
    except sqlite3.error as e:
        print(e)
    
    return conn


def bulkUpdate_helper(id):
    conn = db_connection()
    cursor = conn.cursor()
    sql = '''SELECT %s, %s FROM app_user WHERE %s = ?;'''
    result = cursor.execute(sql % ('access_token','instagram_account_id','id',), (id,))
    tup_res = result.fetchone()
    conn.close()
    #print('tup_res : ', tup_res)
    
    if tup_res is not None:
        try:
            access_token, instagram_account_id = tup_res[0], tup_res[1]
            print('access_token', 'instagram_account_id')
            #print(access_token, instagram_account_id)
            params = getCreds()

            profile_insights = getProfileInsights(params, access_token, instagram_account_id)
            print("profile_insights : ", profile_insights)


            all_user_media_insights = getAllUserMediaInsights(params, access_token, instagram_account_id)
            print("all_user_media_insights : ",all_user_media_insights)

            profile_insights = json.dumps(profile_insights, indent = 4)
            all_user_media_insights = json.dumps(all_user_media_insights, indent = 4)
            
            maintain = {
                        "user_insights": profile_insights.json(),
                        "media_insights": all_user_media_insights.json()#['data']
                        }

            print('maintain ...........................')
            
            print(maintain)

            maintain = json.dumps(maintain, indent = 4)
            
            data = dict()
            
            data['status'] = "Success"
            data['data'] = maintain.json()
            
        except exception as e:
            print('exception: couldnt get instagram media items', e)
            data = {"status": "couldn't get instagram media items"}
        
        # STORE JSON

        data = json.dumps(data, indent = 4)

        filename = 'data/' + str(id) + '.json'
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False)

        print('Saved json {}'.format(id))
    
    # sql = '''UPDATE app_user SET %s = ? WHERE %s = ?;'''
    # print(sql)
    # result = cursor.execute(sql % ('data', 'id',), (str(data), id,))
    # conn.close()

    return


def getAllData_helper(id):
    
    filename = 'data/' + str(id) + '.json'
    
    with open(filename, 'r') as f:
        try:
            data = json.load(f)
        except:
            data = {}

    return data#.json()
