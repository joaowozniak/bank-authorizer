from models.account import Account


class AccountProcess:
    def __init__(self, acc_list):
        self.acc_list = acc_list

    def addAccount(self, account):
        self.acc_list.append(account)

    def getAccountListSize(self):
        return len(self.acc_list)

    def getAccount(self, idx):
        try:
            return self.acc_list[idx]
        except:
            raise ValueError(f"Account {idx} not found")

    def isNewAccount(self):
        return self.getAccountListSize() == 0

    def createAccount(self, account: Account):
        return Account()
