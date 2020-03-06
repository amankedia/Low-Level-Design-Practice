from NewsFeed.model.user import User
from NewsFeed.services.user_post_mapping import UserPost
class UserService(object):
    def createUser(self, name):
        ##Add functionality to check if user already exists
        ##Assumption is that name is user id
        user = User(name)
        UserPost().addUser(name)
        return user

    def addUserFollower(self, userFollwoing, userTofollow):
        userTofollow.addFollower(userFollwoing)
        userFollwoing.addFollowing(userTofollow)