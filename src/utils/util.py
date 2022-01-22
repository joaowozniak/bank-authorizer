from models.account import Account
from models.transaction import Transaction


def getAccount(line) -> Account:
    account = line["account"]
    return Account(**account)


def getTransaction(line) -> Transaction:
    transaction = line["transaction"]
    return Transaction(**transaction)


def getOutputLine(account, violations):
    out = {}
    out_account = {}

    activeCard = account.activeCard
    availableLimit = account.availableLimit

    if activeCard != None and availableLimit != None:
        out_account["activeCard"] = activeCard
        out_account["availableLimit"] = availableLimit

    out["accounts"] = out_account
    out["violations"] = violations

    return out
