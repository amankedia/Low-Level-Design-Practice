from NewsFeed.services.user_post_mapping import UserPost
class NewsFeed(object):

    def displayFeed(self, user, posts):

        feed = set()
        name = user.getName()
        print(name)
        followed_user = user.getFollowing()
        print(followed_user)
        for user in followed_user:
            print(user.getName())
            userPosts = UserPost().getUserPosts(user.getName())
            for post in userPosts:
                feed.add(post.getContent())
        postings = []
        for key in posts:
            postings.append(posts[key])

        sameVotes = []
        diffVotes = []

        for post in postings:
            if post.getUpvotes() == post.getDownvotes():
                sameVotes.append(post)
            else:
                diffVotes.append(post)

        posts = sorted(diffVotes, key = lambda post: post.getUpvotes() - post.getDownvotes(), reverse=True)
        for post in posts:
            feed.add(post.getContent())

        postsBasedOnComment = sorted(sameVotes, key = lambda post: len(post.getComments()), reverse=True)
        for post in postsBasedOnComment:
            feed.add(post.getContent())
        print(feed)