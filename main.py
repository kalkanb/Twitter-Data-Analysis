__author__ = 'Miraç Aknar'
from TwittterFacade import TwitterFacade
tf = TwitterFacade()


results = tf.do_all("halloga")


str1 = "the user: " + results[0].username
str1 += "\n followers count: " + str(results[1]["followers_count"])
str1 += "\n followings count: " + str(results[1]["followings_count"])
str1 += "\n intersection: " + str(results[1]["intersection"])
str1 += "\n"


str1 += "\n hours: "
for i in range(0, 24):
    str1 += "\n" + str(i) + ":" + str(i+1) + " - " + str(results[2]["hours"][i])

str1 += "\n"
str1 += "\n dasy: "
str1 += "\nmonday:" + str(results[2]["days"][1])
str1 += "\ntuesday:" + str(results[2]["days"][2])
str1 += "\nwednesday:" + str(results[2]["days"][3])
str1 += "\nthursday:" + str(results[2]["days"][4])
str1 += "\nfriday:" + str(results[2]["days"][5])
str1 += "\nsaturday:" + str(results[2]["days"][6])
str1 += "\nsunday:" + str(results[2]["days"][0])




str1 += "\n"

str1 += "\n favorites: "


for i in range(0, 10):
    try:
        str1 += ("\n" + str(i) + " - ")
        str1 += results[3]["favorite_users"][i].username + " with "
        str1 += str(results[3]["favorite_numbers"][i]) + " favorites"
    except:
        break



str1 += "\n retweets:"

for i in range(0, 10):
    try:
        str1 += ("\n" + str(i) + " - " )
        str1 += results[4]["retweeted_users"][i].username + " with "
        str1 += str(results[4]["retweeted_numbers"][i]) + " retweets"
    except:
        break





