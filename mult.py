#!/usr/bin/python3

import random
import os
import time

#####
# Constants
#####

defaultProblemCount = 20
correctInARow = 2

#####
# End Constants
#####

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
    
    def isMastered(self, threshold = correctInARow):
        if len(self.attempts) < threshold:
            return False
        
        j = True
        for i in self.attempts[(-1 * correctInARow):]:
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

def generateProblems():
    """Returns a list of all multiplication problems with factors from 1 to 10 (inclusive)"""
    allProblems = []
    for a in range(1,11):
        for b in range(1,11):
            allProblems.append(Problem(a,b))
    return allProblems

def pickStudyProblems(superset, number = defaultProblemCount):
    random.shuffle(superset)
    return superset[0:number]



def askQuestion(problem):
    """
    Asks a the multiplication question in problem and checks for correctness (via problem.attempt()).

    Returns True if correct and False if incorrect.
    """
    def numberInput(problemString):
        """helper function that accepts only integer input"""
        while True:
            try:
                i = int(input(problemString))
                break
            except:
                print("Invalid entry. Try again.")
        return i
    
    attempt = numberInput(str(problem) + " = ")
    return problem.answer(attempt)
    

def clear():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


def printSession(problems):
    sessionTime = time.localtime(time.time())
    filename = str(sessionTime.tm_year) + "_" + str(sessionTime.tm_mon) + "_" + str(sessionTime.tm_mday) + ".md"

    f = open(filename,"w")

    f.write(str(sessionTime))

    for i in problems:
        f.write("### " + str(i))
        f.write("\n")
        for j in i.attempts:
            f.write("-" + str(j))
            f.write("\n")
 
    f.close()

    quit()


def consoleMainLoop():
    problems = pickStudyProblems(generateProblems())
    masteredProblems = []

    while len(problems) != 0:

        tempProblems = problems
        problems = []

        for i in tempProblems:
            if askQuestion(i) is True:    # Asks a question and checks if it is correct
                print("Correct!")
                input("Press return or enter to continue")
            else:
                print("Incorrect! The correct answer is " + i.correctAnswer())
                input("Press return or enter to continue")
            
            # clear the screen
            clear()
            
            #add back only the problems that haven't been mastered
            if i.isMastered() != True:
                problems.append(i)
            else:
                masteredProblems.append(i)
        
        random.shuffle(problems)
        
    printSession(masteredProblems)




consoleMainLoop()
