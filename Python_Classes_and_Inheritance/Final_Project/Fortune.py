
VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here


class WOFPlayer():
    def __init__(self, name) -> None:
        self.name = name
        self.prizes = []
        self.prizeMoney = 0

    def addMoney(self, amt):
        self.prizeMoney += amt

    def goBankrupt(self):
        self.prizeMoney = 0

    def addPrize(self, prize):
        self.prizes.append(prize)

    def __str__(self) -> str:
        return f"{self.name} (${self.prizeMoney})"
# Write the WOFHumanPlayer class definition (part B) here


class WOFHumanPlayer(WOFPlayer):
    def getMove(self, category, obscuredPhrase, guessed):
        self.category = category
        self.obscuredPhrase = obscuredPhrase
        self.guessed = guessed
        print(f"""{self.name} has ({self.prizeMoney} $) 
Category: {self.category} 
Phrase: {self.obscuredPhrase} 
Guessed: {self.guessed}""")
        a = input('Guess a letter, phrase, or type exit or pass:')
        return a
# Write the WOFComputerPlayer class definition (part C) here


class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES = 'ZQXJKVBPYGFWMUCLDRHSNIOATE'

    def __init__(self, name, difficulty):
        WOFPlayer.__init__(self, name)
        self.difficulty = difficulty

    def smartCoinFlip(self):
        rand_number = random.randint(1, 10)
        if self.difficulty > rand_number:
            return True
        elif self.difficulty <= rand_number:
            return False

    def getPossibleLetters(self, guessed=[]):
        lst = []
        for i in LETTERS:
            if self.prizeMoney < VOWEL_COST:
                if i not in guessed and i not in VOWELS:
                    lst.append(i)
            else:
                if i not in guessed:
                    lst.append(i)
        return lst

    def getMove(self, category, obscuredPhrase, guessed=[]):
        possible_letters = self.getPossibleLetters(guessed)
        print(possible_letters)
        if not possible_letters:
            return 'pass'
        else:
            if self.smartCoinFlip():
                for letter in self.SORTED_FREQUENCIES[::-1]:
                    if letter in possible_letters:
                        return letter
            else:
                return random.choice(possible_letters)
