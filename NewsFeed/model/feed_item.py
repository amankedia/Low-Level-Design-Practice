import uuid
import datetime

class FeedItem(object):
    def __init__(self, content):
        self.id = str(uuid.uuid4())
        self.content = content
        self.timestamp = datetime.datetime.now()
        self.comments = []
        self.upvote = 0
        self.downvote = 0

    def getId(self):
        return self.id

    def getContent(self):
        return self.content

    def getTimeStamp(self):
        return self.timestamp

    def getComments(self):
        return self.comments

    def getUpvotes(self):
        return self.upvote

    def getDownvotes(self):
        return self.downvote

    def addComment(self, comment):
        self.comments.append(comment)

    def increaseUpvote(self):
        self.upvote = self.upvote + 1

    def increaseDownvote(self):
        self.downvote = self.downvote + 1