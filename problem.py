import settings

class Problem:
    """
        Class holds a multiplication problem, together with all of the attempts to answer that problem.
    """
    def __init__(self, multiplier, multiplicand):
        self.multiplier = multiplier
        self.multiplicand = multiplicand
        self.timesCorrect = 0
        self.timesIncorrect = 0
        self.attempts = []

    def answer(self, answer):
        """
        Attempts to answer the question. Logs the answer into self.attempts, together with True or False (if correct or incorrect). 
        
        Returns True is correct and False if incorrect.
        """
        if self.multiplicand * self.multiplier == answer:
            self.timesCorrect += 1
            self.attempts.append([answer,True])
            return True
        else:
            self.timesIncorrect += 1
            self.attempts.append([answer,False])
            return False
    
    def isMastered(self, threshold = settings.correctInARow):
        if len(self.attempts) < threshold:
            return False
        
        j = True
        for i in self.attempts[(-1 * threshold):]:
            j = j and i[1];

        return j


    def correctAnswer(self):
        return str(self.multiplicand * self.multiplier)
    
    def __str__(self):
        return str(self.multiplier) + " x " + str(self.multiplicand)
    
    def info(self):
        """Returns the number of times the problem has been solved correctly and incorrectly, as a list."""
        return (self.timesCorrect,self.timesIncorrect)
    

    def debug(self):
        print(self)
        print(self.info())