import os
import pickle
import settings

from problem import *

def initialize():
    """
    Returns a new set of multiplication problems if this is the first use. Otherwise, loads historical problems.
    """
    return generateProblems()
    
    # if os.path.exists(settings.savefile) == False:

def generateProblems():
    """Returns a list of all multiplication problems with factors from 1 to 10 (inclusive)"""
    allProblems = []
    for a in range(1,11):
        for b in range(1,11):
            allProblems.append(Problem(a,b))
    return allProblems    