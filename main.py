__author__ = 'Miraç Aknar'
from TwitterFetcher import TwitterFetcher
from TwitterAnalyzer import TwitterAnalyzer

ta = TwitterAnalyzer()
tf = TwitterFetcher()

the_user = tf.get_twitter_user("peronwho")
print(the_user)
tweets = tf.get_tweets(the_user.twitter_id)

for tw in tweets:
    print(tw.coordinates)





















"""
retweets = tf.get_retweets(the_user.twitter_id)

i= 0
print("retweets:")
for retweet in retweets:
    print(str(i) + " " + str(retweet.target_id) + " " + retweet.text)
    i += 1

retweet_dict = ta.get_most_retweeted(retweets)

favorite_users = retweet_dict["retweeted_users"]
favorite_numbers = retweet_dict["retweeted_numbers"]

for i in range(0, 10):
    print(str(i) + " - "+ favorite_users[i].username + " with " + str(favorite_numbers[i]) + " retweets")












favorites = tf.get_favorites(the_user.twitter_id)

i = 0
print("favorites:")
for favorite in favorites:
    print(str(i) + " " + str(favorite.target_id) + " " + favorite.text)
    i += 1

favorite_dict = ta.get_most_favorited(favorites)

favorite_users = favorite_dict["favorite_users"]
favorite_numbers = favorite_dict["favorite_numbers"]

for i in range(0, 10):
    print(str(i) + " - "+ favorite_users[i].username + " with " + str(favorite_numbers[i]) + " favorites")


"""









"""
followers = tf.get_followers(the_user.twitter_id)

followings = tf.get_followings(the_user.twitter_id)

intersect = ta.get_intersection_of_followers_and_followings(followers, followings)


tweets = tf.get_tweets(the_user.twitter_id)



print("follower : " + str(len(followers)))
print("following : " + str(len(followings)))
print("intersect : " + str(intersect))
hours = ta.get_post_hours(tweets)
print()
i = 1
for hour in hours:
    print(str(i) + ": " + str(hours[i]))
    i += 1





#days = ta.get_post_days(tweets)
"""






"""
print("monday:" + str(days["monday"]))
print("tuesday:" + str(days["tuesday"]))
print("wednesday:" + str(days["wednesday"]))
print("thursday:" + str(days["thursday"]))
print("friday:" + str(days["friday"]))
print("saturday:" + str(days["saturday"]))
print("sunday:" + str(days["sunday"]))
"""






    
"""



"""