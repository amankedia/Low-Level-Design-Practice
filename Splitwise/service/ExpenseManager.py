from Splitwise.models.User import User
from Splitwise.service.ExpenseService import ExpenseService
class ExpenseManager(object):
    def __init__(self):
        self.expenses = []
        self.userMap = {}
        self.balanceSheet = {}

    def addUser(self, user):
        self.userMap[user.getId()] = user
        self.balanceSheet[user.getId()] = {}

    def addExpense(self, expenseType, amount, paidBy, splits, expenseMetadata):
        expense = ExpenseService.createExpense(expenseType, amount, self.userMap.get(paidBy), splits, expenseMetadata)
        self.expenses.append(expense)
        for split in splits:
            paidTo = split.getUser().getId()
            balances = self.balanceSheet.get(paidBy)
            if paidTo not in balances:
                balances.put(paidTo, 0.0)
            balances.put(paidTo, balances.get(paidTo) + split.getAmount())

            balances = self.balanceSheet.get(paidTo)
            if paidBy not in balances:
                balances.put(paidBy, 0)
            balances.put(paidBy, balances.get(paidBy) - split.getAmount())

    def showBalances(self, userId):
        isEmpty = True
        for allBalances in self.balanceSheet:
            for userBalance in allBalances:
                if userBalance > 0:
                    isEmpty = False
                    self.printBalances(allBalances, userBalance)

        if isEmpty:
            print("No balances")

    def printBalances(self, allBalances, userBalance):
        pass
