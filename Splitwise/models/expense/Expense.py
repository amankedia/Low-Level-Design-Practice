from abc import ABC, abstractmethod
import uuid

class Expense(ABC):
    def __init__(self, amount, paidBy, splits, expenseMetadata):
        self.id = str(uuid.uuid4())
        self.amount = amount
        self.paidBy = paidBy
        self.splits = splits
        self.expenseMetadata = expenseMetadata

    def setId(self, id):
        self.id = id

    def getId(self):
        return self.id

    def setAmount(self, amount):
        self.amount = amount

    def getAmount(self):
        return self.amount

    def setPaidBy(self, paidBy):
        self.paidBy = paidBy

    def getPaidBy(self):
        return self.paidBy

    def setSplits(self, splits):
        self.splits = splits

    def getSplits(self):
        return self.splits

    def setExpenseMetadata(self, expenseMetadata):
        self.expenseMetadata = expenseMetadata

    def getExpenseMetadata(self):
        return self.expenseMetadata

    @abstractmethod
    def validate(self):
        pass