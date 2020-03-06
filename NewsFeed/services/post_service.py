from NewsFeed.model.feed_item import FeedItem

class PostService(object):
    posts = []
    def createPost(self, content):
        post = FeedItem(content)
        return post


