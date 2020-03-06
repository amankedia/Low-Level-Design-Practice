class ExpenseMetadata(object):
    def __init__(self, name, imgUrl, notes):
        self.name = name
        self.imgUrl = imgUrl
        self.notes = notes

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setImgUrl(self, imgUrl):
        self.imgUrl = imgUrl

    def getImgUrl(self):
        return self.imgUrl

    def setNotes(self, notes):
        self.notes = notes

    def getNotes(self):
        return self.notes