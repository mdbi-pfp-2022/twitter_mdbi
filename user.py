from tweet import Tweet

class User:

    def __init__(self, username, bio, timeline):
        self.username = username
        self.bio = bio
        self.timeline = timeline
        self.following_users = []

    def follow(self, user):
        self.following_users.append(user)

    def follow_list(self, users):
        self.following_users = self.following_users + users

    def tweet(self, message):
        t = Tweet(message, self, 0)
        self.timeline.tweets.append(t)