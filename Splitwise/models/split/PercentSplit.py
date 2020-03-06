from Splitwise.models.split.Split import Split

class PercentSplit(Split):
    def __init__(self, user, percent):
        super().__init__(user)
        self.percent = percent

    def setPercent(self, percent):
        return self.percent

    def getPercent(self):
        return self.percent