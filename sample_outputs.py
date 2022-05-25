# GET DEBUG ACCESS TOKEN

'''
{'data': {'app_id': '2297717690379584',
  'application': 'Plush',
  'data_access_expires_at': 1660719007,
  'expires_at': 1658126968,
  'granular_scopes': [{'scope': 'pages_show_list',
    'target_ids': ['152766960251161']},
   {'scope': 'instagram_basic', 'target_ids': ['17841448720108201']},
   {'scope': 'instagram_manage_comments', 'target_ids': ['17841448720108201']},
   {'scope': 'instagram_manage_insights', 'target_ids': ['17841448720108201']},
   {'scope': 'instagram_content_publish', 'target_ids': ['17841448720108201']},
   {'scope': 'page_events', 'target_ids': ['152766960251161']},
   {'scope': 'pages_read_engagement', 'target_ids': ['152766960251161']},
   {'scope': 'pages_read_user_content', 'target_ids': ['152766960251161']}],
  'is_valid': True,
  'issued_at': 1652942968,
  'scopes': ['email',
   'pages_show_list',
   'instagram_basic',
   'instagram_manage_comments',
   'instagram_manage_insights',
   'instagram_content_publish',
   'page_events',
   'pages_read_engagement',
   'pages_read_user_content',
   'public_profile'],
  'type': 'USER',
  'user_id': '10159882612522943'}}

'''


# GET INSIGHTS ON IG USER

'''
{'data': [{'description': "Total number of users who have viewed the Business Account's profile within the specified period",
   'id': '17841448720108201/insights/profile_views/day',
   'name': 'profile_views',
   'period': 'day',
   'title': 'Profile Views',
   'values': [{'end_time': '2022-05-18T07:00:00+0000', 'value': 81},
    {'end_time': '2022-05-19T07:00:00+0000', 'value': 0}]},
  {'description': "Total number of times the Business Account's media objects have been uniquely viewed",
   'id': '17841448720108201/insights/reach/day',
   'name': 'reach',
   'period': 'day',
   'title': 'Reach',
   'values': [{'end_time': '2022-05-18T07:00:00+0000', 'value': 12675},
    {'end_time': '2022-05-19T07:00:00+0000', 'value': 0}]},
  {'description': 'Total number of taps on the website link in this profile',
   'id': '17841448720108201/insights/website_clicks/day',
   'name': 'website_clicks',
   'period': 'day',
   'title': 'Website Clicks',
   'values': [{'end_time': '2022-05-18T07:00:00+0000', 'value': 18},
    {'end_time': '2022-05-19T07:00:00+0000', 'value': 0}]}],
 'paging': {'next': 'https://graph.facebook.com/v13.0/17841448720108201/insights?access_token=EAAgpwxa6rUABADp0Fujn4kgPZBfks7NK9ENqdyq8uoVuoDtNZCtwUdxj9mxEDhl8TXhd7Waufumh2WHDAwbZAOLj4BXhpUfiHqmWt7NCOTNsb2a0YubmBbu9cWHrgEPQg9RlnHDtDL9TKCZAKtvFfxqzWWMuZBSwMvwhshdlh6SJk6etOsQTJ8SwTQZCMIElcZD&metric=profile_views%2Creach%2Cwebsite_clicks&period=day&since=1652944772&until=1653117572',
  'previous': 'https://graph.facebook.com/v13.0/17841448720108201/insights?access_token=EAAgpwxa6rUABADp0Fujn4kgPZBfks7NK9ENqdyq8uoVuoDtNZCtwUdxj9mxEDhl8TXhd7Waufumh2WHDAwbZAOLj4BXhpUfiHqmWt7NCOTNsb2a0YubmBbu9cWHrgEPQg9RlnHDtDL9TKCZAKtvFfxqzWWMuZBSwMvwhshdlh6SJk6etOsQTJ8SwTQZCMIElcZD&metric=profile_views%2Creach%2Cwebsite_clicks&period=day&since=1652599170&until=1652771970'}}

'''

# GET ALL MEDIA OF INSTAGRAM

'''
{'data': [
  {'id': '17914861481359553'},
  {'id': '17951850556859622'},
  {'id': '17940845135021613'},
  {'id': '17956610818742858'},
  {'id': '18173970160171350'},
  {'id': '17959352083669817'},
  {'id': '17926513799255600'},
  {'id': '17952811798721472'},
  {'id': '18223483177142287'},
  {'id': '17950868053830668'},
  {'id': '18016075390381771'},
  {'id': '17925678815185081'},
  {'id': '17943932338760096'},
  {'id': '18282805759036937'},
  {'id': '17941377877849237'},
  {'id': '17929248476085028'},
  {'id': '18045636781314601'},
  {'id': '17978121835449315'},
  {'id': '17909701799298071'},
  {'id': '17958868306600356'},
  {'id': '17978776492468918'},
  {'id': '17906181899449108'},
  {'id': '17929588126913044'},
  {'id': '18038508724320308'},
  {'id': '18276149062027466'}
  ],
 'paging': {'cursors': {'after': 'QVFIUlFkT2p1bDVxY213QzU5M2JFWHpKcnBhZATd6MndUUW9zcWczY0VZAcU5ZANXBLazUwc2sxTVhqSFZAmcnRtRWVPQktJRHlsUFZAQUWVXNFpwR2gzaHY5SDJR',
   'before': 'QVFIUk52eS1nWmFnTEJEUlR6aF9KalllMjRFQzQzcWtEaEp0Ni1KUGtrNnVsd1p4cWVMUkJDM1NnbjBWY2tpdXpDY3FUd041VUFmRDFBdlk3QS1DaTFVTlln'},
  'next': 'https://graph.facebook.com/v13.0/17841448720108201/media?access_token=EAAgpwxa6rUABADp0Fujn4kgPZBfks7NK9ENqdyq8uoVuoDtNZCtwUdxj9mxEDhl8TXhd7Waufumh2WHDAwbZAOLj4BXhpUfiHqmWt7NCOTNsb2a0YubmBbu9cWHrgEPQg9RlnHDtDL9TKCZAKtvFfxqzWWMuZBSwMvwhshdlh6SJk6etOsQTJ8SwTQZCMIElcZD&limit=25&after=QVFIUlFkT2p1bDVxY213QzU5M2JFWHpKcnBhZATd6MndUUW9zcWczY0VZAcU5ZANXBLazUwc2sxTVhqSFZAmcnRtRWVPQktJRHlsUFZAQUWVXNFpwR2gzaHY5SDJR'}}

'''

# GET INSIGHTS OF MEDIA

'''
{'data': [{'description': 'Total number of times the media object has been seen',
   'id': '18038508724320308/insights/impressions/lifetime',
   'name': 'impressions',
   'period': 'lifetime',
   'title': 'Impressions',
   'values': [{'value': 1749}]},
  {'description': 'Total number of unique accounts that have seen the media object',
   'id': '18038508724320308/insights/reach/lifetime',
   'name': 'reach',
   'period': 'lifetime',
   'title': 'Reach',
   'values': [{'value': 1659}]}]}

'''

# GET MEDIA DETAILS

'''
{'caption': 'Real Florida Camo Pants 🔥\U0001fab5🍂 Dropping 2/12 🔔 Turn on your post notifications so you don’t miss this drop \n\n#treecamo #realtreecamo #camopants #canvaspants #printpants #printjeans #woods #hunting #fishing #undergroundbrand #undergroundfashion #outfitideas #slowfashion #bestofstreetwear #simplefits #streetwear #winterfashion #winterfashiontrends #springbreak #springseason #spring2022 #shopblack #shopblackowned #shopsmallbusiness #floridafashion #floridacamo #florida #jacksonville #duuuval #alternativefashion',
 'id': '18038508724320308',
 'media_url': 'https://scontent-iad3-1.cdninstagram.com/v/t51.29350-15/273475490_148089197589555_2429374341952437733_n.jpg?_nc_cat=111&ccb=1-7&_nc_sid=8ae9d6&_nc_ohc=zC6QVxhci4sAX9eQr5-&_nc_ht=scontent-iad3-1.cdninstagram.com&edm=AEQ6tj4EAAAA&oh=00_AT-RtbUHTy1GcWIdTjVxTkN9m6xOltLXyiWY1axvXQDHIw&oe=628AA93F',
 'permalink': 'https://www.instagram.com/p/CZsHDaquYhM/',
 'timestamp': '2022-02-07T20:18:32+0000'}

'''

