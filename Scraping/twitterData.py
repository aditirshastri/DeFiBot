import tweepy
# note the twitter api works by using ID, currenlty writing a function to automate this.


print("Starting...")
print("Please generate your own set of credentials on twitter before using this")
# or just reach out to me (Internal only)
# NEEDED TO RUN THIS
# credentials[‘CONSUMER_KEY’]
# credentials[‘CONSUMER_SECRET’]
# credentials[‘ACCESS_TOKEN’]
# credentials[‘ACCESS_SECRET’]

# Input YOUr creds here
auth = tweepy.OAuthHandler(credentials.get(
    'CONSUMER_KEY'), credentials.get('CONSUMER_SECRET'))
auth.set_access_token(credentials.get('ACCESS_TOKEN'),
                      credentials.get('ACCESS_SECRET'))
api = tweepy.API(auth)

# example #1
madhubalaTweetId = '1256174506374291457'
res = api.get_status(madhubalaTweetId, tweet_mode='extended')
print(res.full_text)
