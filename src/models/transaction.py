'''
Define model for transaction.
JSON object example:
{"transaction": {"merchant": "Burger King", "amount": 20, "time": "2019-02-13T11:00:00.000Z"}}
'''

class Transaction:    

    def __init__(self, merchant, amount, time):
        self.merchant = merchant
        self.amount = amount
        self.time = time

    def getMerchant(self):
        return self.merchant

    def getAmount(self):
        return self.amount

    def getTime(self):
        return self.time

  