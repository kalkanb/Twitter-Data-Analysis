__author__ = 'Miraç Aknar'
from TwitterFetcher import TwitterFetcher
from TwitterAnalyzer import TwitterAnalyzer


class TwitterFacade:

    def __init__(self):
        self.twitter_analyzer = TwitterAnalyzer()
        self.twitter_fetcher = TwitterFetcher()

    def do_all(self, username):
        return_list = []
        the_user = self.twitter_fetcher.get_twitter_user(username)
        return_list.append(the_user)
        print("the user created")
        followers = self.twitter_fetcher.get_followers(the_user.twitter_id)
        print("followers created")
        followings = self.twitter_fetcher.get_followings(the_user.twitter_id)

        print("followings created")
        tweets = self.twitter_fetcher.get_tweets(is_retweet=False, twitter_id=the_user.twitter_id)

        i = 0
        print(len(tweets))
        for tw in tweets:
            print(str(i) + " " + tw.text)
            i += 1


        print("tweets created")
        retweets = self.twitter_fetcher.get_tweets(is_retweet=True, twitter_id=the_user.twitter_id)

        i = 0
        print(len(retweets))
        for tw in retweets:
            print(str(i) + " " + tw.text)
            i += 1
        print("retweets created")
        i= 0
        print()

        favorites = self.twitter_fetcher.get_favorites(the_user.twitter_id)
        print("favorites created")


        follow_analysis = {}
        follow_analysis["followers_count"] = the_user.follower_count
        follow_analysis["followings_count"] = the_user.following_count
        follow_analysis["intersection"] = self.twitter_analyzer.get_intersection_of_followers_and_followings(followers, followings)
        print("follow analysis conmpleted")

        tweet_analysis = {}
        tweet_analysis["days"] = self.twitter_analyzer.get_post_days(tweets)
        tweet_analysis["hours"] = self.twitter_analyzer.get_post_hours(tweets)
        print("tweet analysis completed")


        return_list.append(follow_analysis)
        return_list.append(tweet_analysis)
        return_list.append(self.twitter_analyzer.get_most_favorited(favorites))
        print("favorite analysis conmpleted")
        return_list.append(self.twitter_analyzer.get_most_retweeted(retweets))
        print("retweet analysis conmpleted")

        return return_list


