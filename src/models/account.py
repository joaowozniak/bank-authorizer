'''
Define model for account.
JSON object example:
{ "account": { "activeCard": true, "availableLimit": 100 } }
'''

class Account:    

    def __init__(self, activeCard, availableLimit):
        self.activeCard = activeCard
        self.availableLimit = availableLimit
        self.violations = violations

    def isActiveCard(self):
        return self.activeCard

    def getAvailableLimit(self):
        return self.availableLimit

    def setAvailableLimit(self, availableLimit):
        self.availableLimit = availableLimit

    def getViolations(self):
        return self.violations

    def setViolations(self, violations):
        self.violations = violations