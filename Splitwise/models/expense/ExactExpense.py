from Splitwise.models.expense.Expense import Expense
from Splitwise.models.split.ExactSplit import ExactSplit

class ExactExpense(Expense):
    def __init__(self, amount, paidBy, splits, expenseMetadata):
        super().__init__(amount, paidBy, splits, expenseMetadata)

    def validate(self):
        for split in self.splits:
            if not isinstance(split, ExactSplit):
                return False

        amount = self.getAmount()
        sumSplitAmount = 0

        for split in self.splits:
            sumSplitAmount = sumSplitAmount + split.getAmount()

        if sumSplitAmount!=amount:
            return False

        return True