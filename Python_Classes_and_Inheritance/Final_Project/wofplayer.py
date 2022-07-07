class WOFPlayer():
    def __init__(self, name, prizemoney=0, prizes=[]) -> None:
        self.name = name
        self.prizes = []

    def addMoney(self, amt):
        self.prizemoney += amt

    def goBankrupt(self):
        self.prizemoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self) -> str:
        return f"{self.name} ({self.prizemoney} $) - Prizes ({self.prizes})"


alex = WOFPlayer("Alex")
alex.goBankrupt()
alex.addMoney(10)
alex.addMoney(20)
alex.addPrize('Пивко')
print(alex)
