

class Timeline:

    def __init__(self):
        self.tweets = []

    def show_tweets_for_user(self, user):
        for tweet in self.tweets:
            if tweet.user in user.following_users:
                print(tweet.user.username + ": " + tweet.message)

