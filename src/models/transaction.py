from datetime import datetime


class Transaction:
    def __init__(self, merchant, amount, time, isValid=True):
        self.merchant = merchant
        self.amount = amount
        self.time = time
        self.isValid = isValid

    def getMerchant(self):
        return self.merchant

    def getAmount(self):
        return self.amount

    def getTime(self):
        return datetime.fromisoformat(self.time[:-1])

    def setValidation(self, val):
        self.isValid = val
