import tweepy
__author__ = 'Miraç Aknar'


class TwitterConnection:

    def __init__(self):
        self.auth = tweepy.OAuthHandler("noshY0FCaqHWniSu6sUIDQz9U", "36cbIWZxWGqAAjfTve4wb6Wfl9RGHTIWXmgZHbPe9AOdaJDyop")
        self.auth.set_access_token("3907815927-mMraRKELPPQzLBxCScpvcYKHU3WtzoKmHYMeWpd", "fzuN79fZ4jkaOnWOVhwzeUmFQ6WaC90vRaktZQdomidHo")
        self.twitter_api = tweepy.API(self.auth)

    # end