import tweepy
import time

auth = tweepy.OAuthHandler('IBrNk0I2vEkKrWnZwHQGCG4DT',
                           '9tdArBoqFqh8OXVPXFeE25C432CpepILSQCBSnS3W1mBCUNGFo')
auth.set_access_token('1330989669228580864-n3a9hmTfDlkV1UBknwwTcChNKiYD0R',
                      'wsr6ZW6Xiy0N8Zjz5Fe5NtXhubnRzVvU8wJArhORmepLM')

api = tweepy.API(auth)

user = api.me()
print(user.screen_name)


def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(1000)


# generous bot - will follow specific followers
# for follower in limit_handler(tweepy.Cursor(api.followers).items()):
#     if follower.name == 'Nick Meier':
#         follower.follow()


# like a tweet based on a keyword
search_string = 'python'
numberOfTweets = 5

for tweet in tweepy.Cursor(api.search, search_string).items(numberOfTweets):
    try:
        tweet.favorite()
        print('I liked that tweet')
    except tweepy.TweepError as e:
        print(e.reason)
    except StopIteration:
        break
