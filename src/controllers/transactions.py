class TransactionProcess:
    def __init__(self, trans_list):
        self.trans_list = trans_list

    def addTransaction(self, transaction):
        self.trans_list.append(transaction)

    def getTransactionListSize(self):
        return len(self.trans_list)

    def getLastMinutesValidTransactions(self, transaction, delta):
        current_time = transaction.getTime()
        out_trans = []
        for trans in self.trans_list[::-1]:
            time = trans.getTime()
            if time.second > (current_time.second - delta) and trans.isValid:
                out_trans.append(trans)

        return out_trans

    def isHighFrequencySmallInterval(self, transaction, delta=120):
        trans_size = self.getTransactionListSize()
        if trans_size <= 2:
            return False
        else:
            trans = self.getLastMinutesValidTransactions(transaction, delta)

            if len(trans) >= 3:
                return True
            else:
                return False

    def isDoubleTransaction(self, transaction, delta=120):
        trans = self.getLastMinutesValidTransactions(transaction, delta)
        if transaction in trans:
            return True
        else:
            return False
