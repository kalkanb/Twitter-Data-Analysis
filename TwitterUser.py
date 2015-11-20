

class TwitterUser(object):

    def __init__(self, twitter_id=None, username=None, name=None, follower_count=None, following_count=None, profile_picture=None):
        self.twitter_id = twitter_id
        self.username = username
        self.name = name
        self.follower_count = follower_count
        self.following_count = following_count
        self.profile_picture = profile_picture

    # end of init

    def __str__(self):
        return_string = "id: " + str(self.twitter_id)
        return_string += "\nusername: " + str(self.username)
        return_string += "\nname: " + str(self.name)
        return_string += "\nfollowers count: " + str(self.follower_count)
        return_string += "\nfollowings count : " + str(self.following_count)
        return_string += "\nprofile picture : " + str(self.profile_picture)
        return return_string
    # end of str