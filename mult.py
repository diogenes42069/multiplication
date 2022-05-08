#!/usr/bin/python3

import random
import os
import time
import sys

from problem import *
import settings

def generateProblems():
    """Returns a list of all multiplication problems with factors from 1 to 10 (inclusive)"""
    allProblems = []
    for a in range(1,11):
        for b in range(1,11):
            allProblems.append(Problem(a,b))
    return allProblems

def pickStudyProblems(superset, number = settings.defaultProblemCount):
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
            
        if i == -6969:
            sys.exit()

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
