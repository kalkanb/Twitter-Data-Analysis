__author__ = 'Miraç Aknar'
import datetime
from TwitterFetcher import TwitterFetcher

class TwitterAnalyzer:

    def __init__(self):
        self.twitter_fetcher = TwitterFetcher()
    # end

    def get_intersection_of_followers_and_followings(self, followers, followings):
        intersection = 0
        for follower in followers:
            for following in followings:
                if follower.twitter_id == following.twitter_id:
                    intersection += 1
        return intersection
    # end of get_...

    def get_post_days(self, tweets):
        days = [0, 0, 0, 0, 0, 0, 0]
        for tweet in tweets:
            day = datetime.datetime.weekday(tweet.created_at)
            days[day] = days[day] + 1
        return days
    # end of get...

    def get_post_hours(self, tweets):
        hours = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for tweet in tweets:
            hour = tweet.created_at.hour - 7
            hours[hour] += 1
        return hours
    # end

    def get_most_favorited(self, favorites):
        all_favorites = {}
        for favorite in favorites:
            if str(favorite.target_id) in all_favorites.keys():
                all_favorites[str(favorite.target_id)] += 1
            else:
                all_favorites[str(favorite.target_id)] = 1

        sorted_list = sorted(all_favorites, key=lambda key: all_favorites[key], reverse=True)
        users = []
        favorite_numbers = []

        for i in range(0, 10):
            try:
                user = self.twitter_fetcher.get_twitter_user(twitter_id=sorted_list[i])
                users.append(user)
                favorite_numbers.append(all_favorites[sorted_list[i]])
            except:
                break
        return_dict = {"favorite_users": users, "favorite_numbers": favorite_numbers}

        return return_dict

    def get_most_retweeted(self, retweets):

        all_retweeteds = {}
        for retweet in retweets:
            if str(retweet.target_id) in all_retweeteds.keys():
                all_retweeteds[str(retweet.target_id)] += 1
            else:
                all_retweeteds[str(retweet.target_id)] = 1

        sorted_list = sorted(all_retweeteds, key=lambda key: all_retweeteds[key], reverse=True)
        users = []
        retweeted_numbers = []

        for i in range(0, 10):
            try:
                user = self.twitter_fetcher.get_twitter_user(twitter_id=sorted_list[i])
                users.append(user)
                retweeted_numbers.append(all_retweeteds[sorted_list[i]])
            except:
                break
        return_dict = {"retweeted_users": users, "retweeted_numbers": retweeted_numbers}

        return return_dict






