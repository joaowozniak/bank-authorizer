from models.account import Account
from models.transaction import Transaction
from controllers.accounts import AccountProcess
from utils.constant import Constant
from utils.util import *


class Processing:
    def __init__(self, account_proc, trans_proc):
        self.account_proc = account_proc
        self.trans_proc = trans_proc

    def processLine(self, line: str):
        violations = []

        if line.keys().__contains__(Constant.ACCOUNT):
            account = getAccount(line)
            if self.account_proc.isNewAccount():
                self.account_proc.addAccount(account)

            else:
                violations.append(Constant.ACCOUNT_NOT_INITIALIZED)

            return account, violations

        elif line.keys().__contains__(Constant.TRANSACTION):
            transaction = getTransaction(line)

            if self.account_proc.isNewAccount():
                account = Account(activeCard=None, availableLimit=None)
                violations.append(Constant.ACCOUNT_NOT_INITIALIZED)

                return account, violations

            else:
                account = self.account_proc.getAccount(0)

                if not account.isActiveCard:
                    violations.append(Constant.CARD_NOT_ACTIVE)
                    transaction.setValidation(False)

                    return account, violations

                if transaction.getAmount() > account.getAvailableLimit():
                    violations.append(Constant.INSUFFICIENT_LIMIT)
                    transaction.setValidation(False)

                    return account, violations

                if self.trans_proc.isHighFrequencySmallInterval(transaction):
                    violations.append(Constant.HIGH_FREQUENCY_SMALL_INTERVAL)
                    transaction.setValidation(False)

                    return account, violations

                if self.trans_proc.isDoubleTransaction(transaction):
                    violations.append(Constant.DOUBLED_TRANSACTION)
                    transaction.setValidation(False)

                    return account, violations

            self.trans_proc.addTransaction(transaction)
            transaction.setValidation(True)
            amount = account.getAvailableLimit() - transaction.getAmount()
            account.setAvailableLimit(amount)

            return account, violations
