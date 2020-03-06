from Splitwise.models.expense.Expense import Expense
from Splitwise.models.split.EqualSplit import EqualSplit

class EqualExpense(Expense):
    def __init__(self, id, amount, paidBy, splits, expenseMetadata):
        super().__init__(amount, paidBy, splits, expenseMetadata)

    def validate(self):
        for split in self.splits:
            if not isinstance(split, EqualSplit):
                return False
        return True