from NewsFeed.services.user_service import UserService
from NewsFeed.services.post_service import PostService
from NewsFeed.services.user_post_mapping import UserPost
from NewsFeed.services.news_feed import NewsFeed
from NewsFeed.model.feed_item import FeedItem
from NewsFeed.Switcher import Switcher
class Driver(object):

    users = {}
    posts = {}

    def main(self):
        currentUser = ""
        while(True):
            action = str(input())
            action = action.split("~")
            if action[0] == "signup":
                user = UserService().createUser(action[1])
                self.users[user.getName()] = user
                print(self.users)
            elif action[0] == "login":
                currentUser = self.users[action[1]]
                if not currentUser:
                    print("User does not exist")
                print(currentUser)
                NewsFeed().displayFeed(currentUser, self.posts)
            elif action[0] == "post":
                if currentUser == "":
                    print("You need to login first")
                    break
                post = PostService().createPost(action[1])
                UserPost().addUserPosts(currentUser.getName(), post)
                self.posts[post.getId()] = post
                print(self.posts)
            elif action[0] == "upvote":
                post = self.posts[action[1]]
                post.increaseUpvote()
                self.posts[post.getId()] = post
            elif action[0] == "follow":
                userFollowing = self.users[currentUser.getName()]
                userToFollow = self.users[action[1]]
                print(userFollowing.getName(), userToFollow.getName())
                UserService().addUserFollower(userFollowing, userToFollow)
                print(userFollowing.getFollowing(), userToFollow.getFollowers())
            elif action[0] == "reply":
                post = self.posts[action[1]]
                post.addComment(action[2])
            elif action[0] == "shownewsfeed":
                NewsFeed().displayFeed(currentUser, self.posts)
            else:
                print("Please enter appropriate command")



if __name__ == "__main__":
    driver = Driver()
    driver.main()