from NewsFeed.services.user_service import UserService
class Switcher(object):
    def createUser(self, name):
        return UserService.createUser(name)

    def number_0(self):
        return 'zero'

    def number_1(self):
        return 'one'

    def number_2(self):
        return 'two'