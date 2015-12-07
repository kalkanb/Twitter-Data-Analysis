import tweepy
__author__ = 'Miraç Aknar'


class TwitterConnection:

    def __init__(self):

        self.consumer_keys = ["rCfca50ETEOV8VaUWo9poPI0C",
                     "45sMmdZaf4J7RCTrh8zbPHSp2",
                     "noshY0FCaqHWniSu6sUIDQz9U",
                     "3LwzEaSrPampaG8y3mTEZKk3J"]

        self.consumer_secrets = ["4Zx8UvKbK0LOtQyseTnWiEGc4rTpDca4jhEBe1UKBimwXci2tf",
                        "OHIgOIuChXbh3ZhL0EbHVjFTIH3pnlVkKUAu0LDMJTns2DYyfW",
                        "36cbIWZxWGqAAjfTve4wb6Wfl9RGHTIWXmgZHbPe9AOdaJDyop",
                        "tXwWtZngrXlkWQhqnzes5pyEbi6hNecro2pUDpDi4e6W6nwyRW"]

        self.access_tokens = ["4384119929-SR5ea8o7RDZ0wjooj0S6dZWQoxIMlMHoFzmttAc",
                     "2990534891-TNChKXsi3OeeolM7Kh0iy233WGcYTOotAt3NNlr",
                     "3907815927-mMraRKELPPQzLBxCScpvcYKHU3WtzoKmHYMeWpd",
                     "3901212855-6hKxiQ9UeyS5g48qCWmiJjg4VHLSGph9D5lmHrn"]

        self.access_tokens_secrets = ["aTt9NkBQlWBWFV6VhKm0hSLOoFjW0dHr4kWCC3SCNAzJI",
                             "NRH3ZKT0qMRUsnzLREbit3KI8Av89jlaQ4O0CAYMB33V0",
                             "fzuN79fZ4jkaOnWOVhwzeUmFQ6WaC90vRaktZQdomidHo",
                             "RUBpy9UdAMF1uYKKnoLqVQIqkQaFWNGQPnTGHJXtOeVZh"]
        self.index = 0
        self.consumer_key = self.consumer_keys[0]
        self.consumer_secret = self.consumer_secrets[0]
        self.access_token = self.access_tokens[0]
        self.access_token_secret = self.access_tokens_secrets[0]
        self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
        self.auth.set_access_token(self.access_token, self.access_token_secret)
        self.twitter_api = tweepy.API(self.auth)

    # end

    def change_connection_keys(self):
        print("-------------------------------------------connection keys have been changed")
        if self.index is (len(self.consumer_secrets) - 1):
            self.index = 0
            self.consumer_key = self.consumer_keys[0]
            self.consumer_secret = self.consumer_secrets[0]
            self.access_token = self.access_tokens[0]
            self.access_token_secret = self.access_tokens_secrets[0]
            self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
            self.twitter_api = tweepy.API(self.auth)
        else:

            self.consumer_key = self.consumer_keys[self.index + 1]
            self.consumer_secret = self.consumer_secrets[self.index + 1]
            self.access_token = self.access_tokens[self.index + 1]
            self.access_token_secret = self.access_tokens_secrets[self.index + 1]
            self.index = self.index + 1
            self.auth = tweepy.OAuthHandler(self.consumer_key, self.consumer_secret)
            self.auth.set_access_token(self.access_token, self.access_token_secret)
            self.twitter_api = tweepy.API(self.auth)
    # end



