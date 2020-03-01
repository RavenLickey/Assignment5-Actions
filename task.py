import math


def firstrun():
    return "success"


def circleArea(radius):
    return math.pi*radius*radius


def firstLast(theList):
    retList = []
    retList.append(theList[0])
    retList.append(theList[-1])
    return retList
