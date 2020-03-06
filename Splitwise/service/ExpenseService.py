from Splitwise.models.expense.ExactExpense import ExactExpense
from Splitwise.models.expense.EqualExpense import EqualExpense
from Splitwise.models.expense.PercentExpense import PercentExpense
from Splitwise.enumeration.ExpenseType import ExpenseType

class ExpenseService(object):
    def createExpense(self, expenseType, amount, paidBy, splits, expenseMetadata):

        if expenseType == ExpenseType.EXACT:
            return ExactExpense(amount, paidBy, splits, expenseMetadata)
        elif expenseType == ExpenseType.PERCENT:
            for split in splits:
                split.setAmount((amount*split.getPercent())/100.0)
            return PercentExpense(amount, paidBy, splits, expenseMetadata)
        else:
            totalSplits = len(splits)
            splitAmount = (((amount * 100) / totalSplits)) / 100.0
            for split in splits:
                split.setAmount(splitAmount)
            splits[0].setAmount(splitAmount + (amount - splitAmount*totalSplits))
            return EqualExpense(amount, paidBy, splits, expenseMetadata)

