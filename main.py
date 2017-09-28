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


def convertSubsetListIntoEdgesAndTriangles(subsetList):
    edgeList = []
    triangleList = []
    vertexIndexCounter = 0
    edgeIndexCounter = 0
    for subset in subsetList:
        if len(subset) == 2:
            edgeList.append([vertexIndexCounter, vertexIndexCounter + 1])
            vertexIndexCounter = vertexIndexCounter + 2
            edgeIndexCounter = edgeIndexCounter + 1
        if len(subset) == 3:
            triangleList.append([edgeIndexCounter, edgeIndexCounter + 1, edgeIndexCounter + 2])
            edgeList.append([vertexIndexCounter, vertexIndexCounter + 1])
            edgeList.append([vertexIndexCounter, vertexIndexCounter + 2])
            edgeList.append([vertexIndexCounter + 1, vertexIndexCounter + 2])
            vertexIndexCounter = vertexIndexCounter + 3
            edgeIndexCounter = edgeIndexCounter + 3

    return edgeList, triangleList


def drawEdge(screen, color, vertexList, edge):
    pygame.draw.line(screen, color, vertexList[edge[0]], vertexList[edge[1]], 1)


def drawEdges(screen, color, vertexList, edgeList):
    for edge in edgeList:
        drawEdge(screen, color, vertexList, edge)


def drawTriangle(screen, color, vertexList, edgeList, triangle):
    for edge in triangle:
        drawEdge(screen, color, vertexList, edgeList[edge])


def drawTriangles(screen, color, vertexList, edgeList, triangleList):
    for triangle in triangleList:
        drawTriangle(screen, color, vertexList, edgeList, triangle)


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


def main():
    vertexList = generateRandomListOfVertexes(AMOUNT_OF_VERTEXES)
    sortListOfVertexes(vertexList)
    print("vertexList   = " + str(vertexList))
    subsetlist = splitListIntoTripleAndDoubles(vertexList)
    print("subsetList   = " + str(subsetlist))
    edgeList, triangleList = convertSubsetListIntoEdgesAndTriangles(subsetlist)
    print("edgeList     = " + str(edgeList))
    print("triangleList = " + str(triangleList))
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    screen.fill(White)
    drawVertexesFromList(screen, Blue, vertexList)
    drawInitialEdges(screen, Red, subsetlist)

    drawEdges(screen, Blue, vertexList, edgeList)
    drawTriangles(screen, Yellow, vertexList, edgeList, triangleList)
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                # if event.type==KEYDOWN:
                #   return# main()

        pygame.display.update()


main()
