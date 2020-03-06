
class UserPost(object):

    users = {}
    posts = []

    def addUser(self, user_name):
        self.users[user_name] = []

    def addUserPosts(self, user_name, post):
        self.users[user_name].append(post)

    def getUserPosts(self, user_name):
        return self.users[user_name]