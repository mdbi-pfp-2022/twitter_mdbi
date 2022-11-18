

class Tweet:

    def __init__(self, message, user, timestamp):
        if len(message) > 280:
            raise Exception("tweets mustn't be longer than 280 chars")

        self.message = message
        self.user = user
        self.timestamp = timestamp
