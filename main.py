__author__ = 'Miraç Aknar'
from TwitterFetcher import TwitterFetcher


tf = TwitterFetcher()

the_user = tf.get_twitter_user("halloga")
#print(the_user)

followers = tf.get_followers(the_user.twitter_id)

i = 0
for follower in followers:
    print(str(i) + " " + follower.username + " " + follower.name + " " + str(follower.twitter_id))
    i+= 1

#followings = tf.get_followings(the_user.twitter_id)

#for following in followings:
#    print(str(i) + " " + following.username + " " + str(following.twitter_id))
#    i+= 1

#tweets = tf.get_tweets(the_user.twitter_id)

#for tweet in tweets:foll
#    print(str(i) + " " +  tweet.text)
#    i += 1

#favorites = tf.get_favorites(the_user.twitter_id)

#for favorite in favorites:
#    print(str(i) + " " + str(favorite.target_id) +  " " +  favorite.text)
#    i += 1

#retweets = tf.get_retweets(the_user.twitter_id)

#for retweet in retweets:
#    print(str(i) + " " + str(retweet.target_id) +  " " +  retweet.text)
#    i += 1