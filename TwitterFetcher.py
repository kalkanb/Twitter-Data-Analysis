__author__ = 'Miraç Aknar'
from TwitterUser import TwitterUser
from TwitterConnection import TwitterConnection
from Tweet import Tweet
import tweepy


class TwitterFetcher(object):

    def __init__(self):
        self.twitter_connection = TwitterConnection()
    # end

    def get_twitter_user(self, twitter_id=None, username=None):
        twitter_user = TwitterUser()
        try:
            if twitter_id is not None:
                api_twitter_user = self.twitter_connection.twitter_api.get_user(twitter_id)
                twitter_user = TwitterUser(api_twitter_user.id, api_twitter_user.screen_name, api_twitter_user.name,  api_twitter_user.followers_count, api_twitter_user.friends_count, api_twitter_user.profile_image_url)
            else:
                api_twitter_user = self.twitter_connection.twitter_api.get_user(username)
                twitter_user = TwitterUser(api_twitter_user.id, api_twitter_user.screen_name, api_twitter_user.followers_count, api_twitter_user.friends_count, api_twitter_user.profile_image_url)
        except:
            self.twitter_connection.change_connection_keys()
            self.get_twitter_user(twitter_id, username)

        return twitter_user
    # end of get_twitter_user

    def get_followers(self, twitter_id):
        the_user = self.get_twitter_user(twitter_id=twitter_id)
        if the_user.follower_count > 400:
            followers = self.get_followers_big(twitter_id=twitter_id)
        else:
            followers = self.get_followers_small(twitter_id=twitter_id)

        return followers

    def get_followings(self, twitter_id):
        the_user = self.get_twitter_user(twitter_id=twitter_id)
        if the_user.following_count > 400:
            followings = self.get_followings_big(twitter_id=twitter_id)
        else:
            followings = self.get_followings_small(twitter_id=twitter_id)

        return followings



    def get_followers_small(self, twitter_id):

        followers = []
        followersapi = None

        check1 = True
        while(check1):
            try:
                followersapi = tweepy.Cursor(self.twitter_connection.twitter_api.followers, user_id=twitter_id).items()

                for user in followersapi:
                    twitter_user = TwitterUser()
                    twitter_user.name = user.name
                    twitter_user.twitter_id = user.id
                    twitter_user.username = user.screen_name
                    followers.append(twitter_user)
                check1 = False
            except:
                self.twitter_connection.change_connection_keys()

        return followers
    # end of get_small_followers

    def get_followers_big(self, twitter_id):
        followers = []

        ids = None
        check1 = True
        while check1:
            try:
                print("denedik")
                ids = self.twitter_connection.twitter_api.followers_ids(twitter_id)
                print("denedik oldu")
                check1 = False
            except:
                self.twitter_connection.change_connection_keys()

        for id in ids:
            check2 = True
            while check2:
                try:
                    print(str(id))
                    twitter_user =self.get_twitter_user(twitter_id=id)
                    followers.append(twitter_user)
                    print(twitter_user.username)
                    check2= False
                except:
                    self.twitter_connection.change_connection_keys()

        return followers


    def get_followings_small(self, twitter_id):

        followings = []
        followingsapi = None

        check1 = True
        while(check1):
            try:
                followingsapi = tweepy.Cursor(self.twitter_connection.twitter_api.friends, user_id=twitter_id).items()
                for user in followingsapi:
                    twitter_user = TwitterUser()
                    twitter_user.name = user.name
                    twitter_user.twitter_id = user.id
                    twitter_user.username = user.screen_name
                    followings.append(twitter_user)
                check1 = False
            except:
                self.twitter_connection.change_connection_keys()



        return followings
    # end of get_followings

    def get_followings_big(self, twitter_id):
        followings = []

        ids = None
        check1 = True
        while check1:
            try:
                print("denedik")
                ids = self.twitter_connection.twitter_api.frineds_id(twitter_id)
                print("denedik oldu")
                check1 = False
            except:
                self.twitter_connection.change_connection_keys()

        for id in ids:
            check2 = True
            while check2:
                try:
                    print(str(id))
                    twitter_user =self.get_twitter_user(twitter_id=id)
                    followings.append(twitter_user)
                    print(twitter_user.username)
                    check2= False
                except:
                    self.twitter_connection.change_connection_keys()

        return followings








    def get_favorites(self, twitter_id):
        favorites = []
        try:
            for i in range(1, 7):

                check1 = True
                while check1:
                    try:
                        favs = self.twitter_connection.twitter_api.favorites(id = twitter_id, page=i)
                        check1 = False
                        for fav in favs:
                            tweet = Tweet()
                            tweet.source_id = twitter_id
                            tweet.text = fav.text
                            tweet.target_id = fav.author.id
                            favorites.append(tweet)
                            if len(favorites) == 100:
                                break

                        check1 = False
                    except:
                        self.twitter_connection.change_connection_keys()
        except:
            return favorites
        return favorites


    def get_tweets(self, is_retweet, twitter_id):
        tweets = []
        numberOfPage = None
        checkstuff = 0

        if is_retweet: # ordinary tweet
            numberOfPage = 50

        else:
            numberOfPage = 20

        for i in range(1, numberOfPage):
            if checkstuff:
                break

            check1 = True
            stuff = None

            while check1:
                try:
                    stuff = self.twitter_connection.twitter_api.user_timeline(id=twitter_id, page=i)
                    if len(tweets) > 100:
                        break

                    if len(stuff) == 0:
                        checkstuff = True
                        break

                    for tw in stuff:
                        tweet = Tweet()
                        if is_retweet:
                            if tw.text[0] is "R" and tw.text[1] is "T":
                                author = tw.text[4:len(tw.text)].split(':')[0]
                                try:
                                    author_id = self.twitter_connection.twitter_api.get_user(screen_name=author).id
                                    tweet.source_id = twitter_id
                                    tweet.target_id = author_id
                                    tweet.text = tw.text
                                    tweets.append(tweet)

                                except:
                                    pass
                        else:
                            if tw.text[0] is not "R" and tw.text[1] is not "T":
                                tweet.text = tw.text
                                tweet.source_id = twitter_id
                                tweet.target_id = 0
                                tweet.created_at = tw.created_at
                                tweets.append(tweet)


                    check1 = False

                except:
                    self.twitter_connection.change_connection_keys()

        return tweets
""""
    def get_tweets(self, twitter_id):

        tweets = []
        for i in range(1, 20):

            check1 = True
            stuff = None

            while check1:
                try:
                    stuff = self.twitter_connection.twitter_api.user_timeline(id=twitter_id, page=i)
                    check1 = False
                    for tw in stuff:
                        tweet = Tweet()
                        if tw.text[0] is not "R" and tw.text[1] is not "T":
                            tweet.text = tw.text
                            tweet.source_id = twitter_id
                            tweet.target_id = 0
                            tweet.created_at = tw.created_at
                            tweets.append(tweet)
                        if len(tweets) > 100:
                            break
                    if len(tweets) > 100:
                        break
                except:
                    self.twitter_connection.change_connection_keys()

        return tweets

    def get_retweets(self, twitter_id):
        retweets = []
        checkstuff = False
        for i in range(1, 50):
            if checkstuff:
                break

            check1 = True
            stuff = None

            while check1:
                try:
                    stuff = self.twitter_connection.twitter_api.user_timeline(id=twitter_id, page=i)
                    if len(retweets) > 100:
                        break

                    if len(stuff) == 0:
                        checkstuff = True
                        break

                    check1 = False

                    for tw in stuff:
                        tweet = Tweet()
                        if tw.text[0] is "R" and tw.text[1] is "T":
                            author = tw.text[4:len(tw.text)].split(':')[0]
                            try:
                                author_id = self.twitter_connection.twitter_api.get_user(screen_name=author).id
                                tweet.source_id = twitter_id
                                tweet.target_id = author_id
                                tweet.text = tw.text
                                retweets.append(tweet)
                            except:
                                pass

                except:
                    self.twitter_connection.change_connection_keys()





        return retweets



"""""