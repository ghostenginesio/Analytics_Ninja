import requests
import json


'''
INITIAL URL

https://www.facebook.com/v13.0/dialog/oauth?
  client_id=2297717690379584
  &redirect_uri=https://analyticsninja.herokuapp.com/callback_token
  &state="st=state123abc,ds=123456789"
  &display=popup
  &scope=email%20public_profile%20instagram_basic%20instagram_content_publish%20instagram_manage_comments%20instagram_manage_insights%20pages_read_engagement%20pages_show_list
  &response_type=code

'''


# MAKE API CALLS

def makeAPICalls(url, endpointParams, debug = 'no'):
    
    data = requests.get(url, endpointParams)
    
    print(data.content)

    return json.loads(data.content)


# CREDENTIALS

def getCreds():
    
    params = dict()
    #params['client_id'] = '392864249398762'                  # client id
    #params['client_secret'] = '8d6a8470330761066754fd9d53dd2e10'     # client secret
    params['client_id'] = '2297717690379584'                  # client id
    params['client_secret'] = '93c97415a01a82675f61dba8ebc67eca'     # client secret
    params['graph_domain'] = 'https://graph.facebook.com'
    params['graph_version'] = 'v13.0'
    params['endpoint_base'] = params['graph_domain'] + '/' + params['graph_version'] + '/'
    params['debug'] = 'no'
    params['redirect_uri'] = ''
    params['code'] = ''
    params['access_token'] = ''        # access token
    params['user_id'] = ''
    
    return params


# EXCHANGE CODE FOR ACCESS TOKEN

def getAccessToken(params, code):
    
    endpointParams = dict()
    url = params['endpoint_base'] + 'oauth/access_token'
    endpointParams['redirect_uri'] = '''http://167.99.183.60:5001/callback_token'''
    endpointParams['client_id'] = params['client_id']
    endpointParams['client_secret'] = params['client_secret']
    endpointParams['code'] = code
    
    return makeAPICalls(url, endpointParams)    


# GET DEBUG TOKENS AND USER ID

def getDebugToken(params, access_token):
    
    endpointParams = dict()
    endpointParams['input_token'] = params['access_token']
    endpointParams['access_token'] = access_token
    url = params['graph_domain'] + '/debug_token'
    
    return makeAPICalls(url, endpointParams)


# EXCHANGE ACCESS TOKENS TO LIFETIME

def getLifetimeToken(params, access_token):
    
    endpointParams = dict() 
    endpointParams['grant_type'] = 'fb_exchange_token'
    endpointParams['client_id'] = params['client_id']
    endpointParams['client_secret'] = params['client_secret']
    endpointParams['fb_exchange_token'] = access_token
    url = params['endpoint_base'] + 'oauth/access_token'
    
    return makeAPICalls(url, endpointParams)


# GET INSTAGRAM USER ID AND NAME

def getInstagramCreds(params, access_token):
    
    url = params['graph_domain'] + '/' + params['graph_version'] + '/' + params['user_id']
    endpointParams = dict() 
    endpointParams['fields'] = 'id,username'
    endpointParams['access_token'] = access_token
    
    return makeAPICalls(url, endpointParams)        



# GET SELF DETAILS - USER ID

def selfDetails(params, access_token):

    url = params['graph_domain'] + '/me'
    endpointParams = dict()
    endpointParams['access_token'] = access_token

    return makeAPICalls(url, endpointParams)


# GET SELF DETAILS - USER ACCOUNT DETAILS

def selfDetailsAccounts(params, access_token):

    url = params['graph_domain'] + '/me/accounts'
    endpointParams = dict()
    endpointParams['access_token'] = access_token
    endpointParams['fields'] = 'name,id,instagram_business_account'

    return makeAPICalls(url, endpointParams)


# GET ALL MEDIA OF INSTAGRAM

def getAllMedia(params, access_token, instagram_account_id):
    url = params['endpoint_base'] + str(instagram_account_id) + '/media'
    endpointParams = dict()
    endpointParams['access_token'] = access_token
    return makeAPICalls(url, endpointParams)


# GET MEDIA DETAILS
 
def getMediaDetails(params, access_token, media_id):
    url = params['endpoint_base'] + str(media_id)
    endpointParams = dict()
    endpointParams['access_token'] = access_token
    endpointParams['fields'] = 'id,media_url,permalink,timestamp,caption'
    return makeAPICalls(url, endpointParams)         

# GET COMPLETE MEDIA INSIGHTS

def getMediaInsights(params, access_token, instagram_account_id, media_id):

    media_full = dict()
    media_full['instagram_account_id'] = instagram_account_id
    media_full['media_id'] = media_id
    params['access_token'] = access_token

    url = params['endpoint_base'] + str(media_id)
    
    try:
      endpointParams = dict()
      endpointParams['fields'] = 'id,media_url,permalink,timestamp,caption'
      endpointParams['access_token'] = params['access_token']
      media_details = makeAPICalls(url, endpointParams)
      media_full['caption'] = media_details['caption']
      media_full['media_url'] = media_details['media_url']
      media_full['timestamp'] = media_details['timestamp']  
    except:
      pass  

    url = params['endpoint_base'] + str(media_id) + '/insights'

    try:
      endpointParams = dict()
      endpointParams['metric'] = 'impressions'
      endpointParams['period'] = 'lifetime' 
      endpointParams['access_token'] = params['access_token'] 
      impressions = makeAPICalls(url, endpointParams)
      media_full['impressions'] = impressions['data'][0]['values'][0]['value']
    except:
      pass  

    try:
      endpointParams = dict()
      endpointParams['metric'] = 'reach'
      endpointParams['access_token'] = params['access_token']
      reach = makeAPICalls(url, endpointParams)
      media_full['reach'] = reach['data'][0]['values'][0]['value']
    except:
      pass  

    try:
      endpointParams = dict()
      endpointParams['metric'] = 'engagement'
      endpointParams['access_token'] = params['access_token']
      engagement = makeAPICalls(url, endpointParams)
      media_full['engagement'] = engagement['data'][0]['values'][0]['value']
    except:
      pass  

    try:
      endpointParams = dict()
      endpointParams['metric'] = 'saved'
      endpointParams['access_token'] = params['access_token']
      saved = makeAPICalls(url, endpointParams)
      media_full['saved'] = saved['data'][0]['values'][0]['value']
    except:
      pass  
    
    
    print(media_full)

    return media_full.json()


# GET ALL USER MEDIA INSIGHTS AND STORE


def getAllUserMediaInsights(params, access_token, instagram_account_id):
    ids = getAllMedia(params, access_token, instagram_account_id)
    print('ids : ', ids)
    arr = []
    for elem in ids['data']:
        media_id = elem['id']
        arr.append(getMediaInsights(params, access_token, instagram_account_id, media_id))

    return {"data": arr}

def getProfileInsights(params, access_token, instagram_account_id):
    
    account_full = dict()
    account_full['instagram_account_id'] = instagram_account_id
    params['access_token'] = access_token

    url = params['endpoint_base'] + str(instagram_account_id) + '/insights'
    
    try:
      endpointParams = dict()
      endpointParams['metric'] = 'impressions'
      endpointParams['period'] = 'day' 
      endpointParams['access_token'] = params['access_token'] 
      impressions =  makeAPICalls(url, endpointParams)
      impressions = impressions['data'][0]['values'][0]['value']
      account_full['impressions'] = impressions
    except:
      pass
    

    try:
      endpointParams = dict()
      endpointParams['metric'] = 'reach'
      endpointParams['period'] = 'day' 
      endpointParams['access_token'] = params['access_token'] 
      reach =  makeAPICalls(url, endpointParams)
      reach = reach['data'][0]['values'][0]['value']
      account_full['reach'] = reach
    except:
      pass  
    

    try:
      endpointParams = dict()
      endpointParams['metric'] = 'profile_views'
      endpointParams['period'] = 'day'
      endpointParams['access_token'] = params['access_token'] 
      profile_views =  makeAPICalls(url, endpointParams)
      profile_views = profile_views['data'][0]['values'][0]['value']
      account_full['profile_views'] = profile_views
    except:
      pass  
    
    try:
      endpointParams = dict()
      endpointParams['metric'] = 'website_clicks'
      endpointParams['period'] = 'day' 
      endpointParams['access_token'] = params['access_token'] 
      website_clicks =  makeAPICalls(url, endpointParams)
      website_clicks = website_clicks['data'][0]['values'][0]['value']
      account_full['website_clicks'] = website_clicks
    except:
      pass  
    
    try:
      endpointParams = dict()
      endpointParams['metric'] = 'follower_count'
      endpointParams['period'] = 'day' 
      endpointParams['access_token'] = params['access_token'] 
      follower_count =  makeAPICalls(url, endpointParams)
      follower_count = follower_count['data'][0]['values'][0]['value']
      account_full['follower_count'] = follower_count
    except:
      pass  
    
    try:
      followers_per_impression = follower_count/impressions * 100
      account_full['followers_per_impression'] = followers_per_impression
    except:
      pass  

    try:
      website_taps_per_impression = website_clicks/impressions * 100
      account_full['website_taps_per_impression'] = website_taps_per_impression
    except:
      pass  
    
    try:
      visits_per_impression = profile_views/impressions * 100
      account_full['visits_per_impression'] = visits_per_impression
    except:
      pass  
    
    print(account_full)

    return account_full.json()

