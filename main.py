SCREEN_WIDTH = 512  # 500
SCREEN_HEIGHT = 512  # 400
AMOUNT_OF_VERTEXES = 10

########Colors########
Aqua = (0, 255, 255)
Black = (0, 0, 0)
Blue = (0, 0, 255)
Fuchsia = (255, 0, 255)
Gray = (128, 128, 128)
Green = (0, 128, 0)
Lime = (0, 255, 0)
Maroon = (128, 0, 0)
NavyBlue = (0, 0, 128)
Olive = (128, 128, 0)
Purple = (128, 0, 128)
Red = (255, 0, 0)
Silver = (192, 192, 192)
Teal = (0, 128, 128)
White = (255, 255, 255)
Yellow = (255, 255, 0)
########Colors########


import pygame, sys
from pygame.locals import *
import random


def generateRandomListOfVertexes(amount):
    list = []
    for i in range(0, amount):
        x = random.randrange(0, SCREEN_WIDTH)
        y = random.randrange(0, SCREEN_HEIGHT)
        list.append([x, y])
    return list


def sortListOfVertexes(list):
    list.sort()


def splitListIntoTripleAndDoubles(list, finishedList=[]):
    firstHalf = list[:round(len(list) / 2)]
    secondHalf = list[round(len(list) / 2):]
    if len(firstHalf) > 3:
        firstHalf = splitListIntoTripleAndDoubles(firstHalf, finishedList)
    if len(secondHalf) > 3:
        secondHalf = splitListIntoTripleAndDoubles(secondHalf, finishedList)
    if len(firstHalf) <= 3:
        finishedList.append(firstHalf)
    if len(secondHalf) <= 3:
        finishedList.append(secondHalf)
    if len(firstHalf) <= 3 and len(secondHalf) <= 3:  # len(list):
        return list
    else:
        return finishedList


def drawVertexesFromList(screen, color, list):
    for vertex in list:
        pygame.draw.circle(screen, color, vertex, 3)


def drawInitialEdges(screen, color, subsetlist):
    for subset in subsetlist:
        if len(subset) == 2:
            pygame.draw.line(screen, color, subset[0], subset[1], 1)
        if len(subset) == 3:
            pygame.draw.polygon(screen, color, subset, 1)


def getBaseLREdge(leftTriangulation, rightTriangulation):
    return  # todo


def drawMergedEdges(screen, color, subsetlist):
    for i in range(0, len(subsetlist)):
        baseLREdge = getBaseLREdge(subsetlist[i], subsetlist[i + 1])
        pygame.draw.line(screen, color, baseLREdge)
        # pygame.draw.line(screen, color, subsetlist[0][0], subsetlist[1][0], 1)
        # pygame.draw.line(screen, color, subsetlist[0][0], subsetlist[1][1], 1)


def main():
    list = generateRandomListOfVertexes(AMOUNT_OF_VERTEXES)
    sortListOfVertexes(list)
    print(list)
    subsetlist = splitListIntoTripleAndDoubles(list)
    print(subsetlist)

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    screen.fill(White)
    drawVertexesFromList(screen, Blue, list)
    drawInitialEdges(screen, Red, subsetlist)
    drawMergedEdges(screen, Green, subsetlist)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                # if event.type==KEYDOWN:
                #   return# main()

        pygame.display.update()


main()
