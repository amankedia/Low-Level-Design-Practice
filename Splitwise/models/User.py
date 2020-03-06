class User(object):
    def __init__(self, id, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.id = id

    def getId(self):
        return self.id

    def setId(self, id):
        self.id = id

    def setName(self, name):
        self.name = name

    def getName(self, name):
        return self.name

    def setPhone(self, phone):
        self.phone = phone

    def getPhone(self):
        return self.phone

    def getEmail(self):
        return self.email

    def setEmail(self, email):
        self.email = email