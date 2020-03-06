from Splitwise.models.expense.Expense import Expense
from Splitwise.models.split.PercentSplit import PercentSplit

class PercentExpense(Expense):
    def __init__(self, amount, paidBy, splits, expenseMetadata):
        super().__init__(amount, paidBy, splits, expenseMetadata)

    def validate(self):
        for split in self.splits:
            if not isinstance(split, PercentSplit):
                return False

        totalPercent = 100
        sumSplitPercent = 0

        for split in self.splits:
            sumSplitPercent = sumSplitPercent + split.getPercent()

        if sumSplitPercent!=totalPercent:
            return False

        return True