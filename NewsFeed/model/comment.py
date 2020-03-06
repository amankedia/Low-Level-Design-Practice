class Comment(object):
    def __init__(self, content):
        self.content = content
        ##Add comment on comment, upvote, downvote features here

    def getCommentContent(self):
        return self.content