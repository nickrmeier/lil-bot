import tweepy

auth = tweepy.OAuthHandler('IBrNk0I2vEkKrWnZwHQGCG4DT',
                           '9tdArBoqFqh8OXVPXFeE25C432CpepILSQCBSnS3W1mBCUNGFo')
auth.set_access_token('1330989669228580864-DNJFVz3PTTcsXCvN0CEdtZVL4T5N4N',
                      'wwZIl44gDCkUuWG7nkPnCfchKz8MGj0zNhJXUOl6CjtNh')

api = tweepy.API(auth)

user = api.me()
print(user.screen_name)
