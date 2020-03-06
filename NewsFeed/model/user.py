class User(object):

    def __init__(self, name):
        self.name = name
        self.followers = []
        self.following = []

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def addFollower(self, follower):
        self.followers.append(follower)

    def getFollowers(self):
        return self.followers

    def addFollowing(self, following):
        self.following.append(following)

    def getFollowing(self):
        return self.following