__author__ = 'Miraç Aknar'


class Tweet(object):

    def __init__(self, text=None, target_id=None, source_id=None, created_at=None, is_retweeted=None):
        self.source_id = source_id
        self.target_id = target_id
        self.text = text
        self.created_at = created_at
        self.is_retweeted = is_retweeted
    # end














