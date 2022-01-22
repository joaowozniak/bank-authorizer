class Account:
    def __init__(self, activeCard, availableLimit):
        self.activeCard = activeCard
        self.availableLimit = availableLimit

    def isActiveCard(self):
        return self.activeCard

    def getAvailableLimit(self):
        return self.availableLimit

    def setAvailableLimit(self, availableLimit):
        self.availableLimit = availableLimit
