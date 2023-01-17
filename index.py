import tweepy
import os
# your Twitter API key and API secret
# my_api_key = "9CAaX7JhSBTue5gstg7Z2eoLu"
# my_api_secret = "JDoktGlWfPq2m7kbHLlkjErrn2qnyr9QzDZiWCBr9IqYAH5DGX"

os.environ['TOKEN'] = 'AAAAAAAAAAAAAAAAAAAAAFCWxQAAAAAAIAmrP66R94LAZItXGM0zqKmlQGg%3DPhkFm8c0IkOBnidQWeXJccF4SoTrZpt6gUIQEuL7yeojeRjU2N'

def auth():
    return os.getenv('TOKEN')

def create_headers(bearer_token):
    headers = {"Authorization": "Bearer {}".format(bearer_token)}
    return headers

def create_url(keyword, start_date, end_date, max_results = 10):
    
    search_url = "https://api.twitter.com/2/tweets/search/all" #Change to the endpoint you want to collect data from

    #change params based on the endpoint you are using
    query_params = {'query': keyword,
                    'start_time': start_date,
                    'end_time': end_date,
                    'max_results': max_results,
                    'expansions': 'author_id,in_reply_to_user_id,geo.place_id',
                    'tweet.fields': 'id,text,author_id,in_reply_to_user_id,geo,conversation_id,created_at,lang,public_metrics,referenced_tweets,reply_settings,source',
                    'user.fields': 'id,name,username,created_at,description,public_metrics,verified',
                    'place.fields': 'full_name,id,country,country_code,geo,name,place_type',
                    'next_token': {}}
    return (search_url, query_params)
