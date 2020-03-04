import pygame as pyg
import sys
import numpy as np
from pygame.locals import *
import math
import heapq as hpq
import re
import copy

#need to figure out how to set up equation
def SolveLine(point1, point2):
    m = (point2[1]-point1[1])/(point2[0]-point1[0])
    b = point1[1]-m*point1[0]
    return m, b

def CreateRect(map_space):
    lines = []
    rect_coords = [(38, 126),
                   (29, 131),
                   (29, 131),
                   (94, 169),
                   (94, 169),
                   (103, 164),
                   (103, 164),
                   (38, 126)]
    for n in range(0, len(rect_coords), 2):
        m, b= SolveLine(rect_coords[n], rect_coords[n + 1])
        line = []
        for x in range(0, 300):
            y = m * x + b
            line.append(y)
        lines.append([line])   
    for key in map_space.keys():
        if (key[1] >= lines[0][0][key[0]]):
            if (key[1] <= lines[1][0][key[0]]):
                if (key[1] <= lines[2][0][key[0]]):
                    if (key[1] >= lines[3][0][key[0]]):
                        map_space[key] = 0
    return map_space

def CreateRhombus(map_space):   
    lines = []
    #rhomb_coords = [(199, 174), (224, 159), (249, 174), (224, 189)]
    rhomb_coords = [(224, 159),
                    (199, 174),
                    (199, 174),
                    (224, 189),
                    (224, 189),
                    (249, 174),
                    (249, 174),
                    (224, 159)]
    for n in range(0, len(rhomb_coords), 2):
        m, b= SolveLine(rhomb_coords[n], rhomb_coords[n + 1])
        line = []
        for x in range(0, 300):
            y = m * x + b
            line.append(y)
        lines.append([line])   
    for key in map_space.keys():   
        if key[1] >= lines[0][0][key[0]]:
            if key[1] <= lines[1][0][key[0]]:
                if key[1] <= lines[2][0][key[0]]:
                    if key[1] >= lines[3][0][key[0]]:
                        map_space[key] = 0
    return map_space

def CreatePoly1(map_space):   
    lines = []
    #poly1_coords = [(22.5, 50), (50, 50), (20, 80)]
    poly1_coords = [(22.5, 50),
                    (20, 80),
                    (20, 80),
                    (50, 50),
                    (50, 50),
                    (22.5, 50)]
    for n in range(0, len(poly1_coords), 2):
        m, b= SolveLine(poly1_coords[n], poly1_coords[n + 1])
        line = []
        for x in range(0, 300):
            y = m * x + b
            line.append(y)
        lines.append([line])   
    for key in map_space.keys():
        if key[1] >= lines[0][0][key[0]]:
            if key[1] <= lines[1][0][key[0]]:
                if key[1] >= lines[2][0][key[0]]:
                        map_space[key] = 0
    return map_space

def CreatePoly2(map_space):   
    lines = []
    #poly2_coords = (50, 50), (75, 80), (100, 50)
    poly2_coords = [(50, 50),
                    (75, 80),
                    (75, 80),
                    (100, 50),
                    (100, 50),
                    (50, 50)]
    for n in range(0, len(poly2_coords), 2):
        m, b= SolveLine(poly2_coords[n], poly2_coords[n + 1])
        line = []
        for x in range(0, 300):
            y = m * x + b
            line.append(y)
        lines.append([line])   
    for key in map_space.keys():
        if key[1] <= lines[0][0][key[0]]:
            if key[1] <= lines[1][0][key[0]]:
                if key[1] >= lines[2][0][key[0]]:
                        map_space[key] = 0
    return map_space

def CreatePoly3(map_space):   
    lines = []
    #poly3_coords = [(25, 15), (22.5, 50), (100, 50), (75, 15)]
    poly3_coords = [(25, 15),
                    (22.5, 50),
                    (22.5, 50),
                    (100, 50),
                    (100, 50),
                    (75, 15),
                    (75, 15),
                    (25, 15)]
    for n in range(0, len(poly3_coords), 2):
        m, b= SolveLine(poly3_coords[n], poly3_coords[n + 1])
        line = []
        for x in range(0, 300):
            y = m * x + b
            line.append(y)
        lines.append([line])   
    for key in map_space.keys():
        if key[1] >= lines[0][0][key[0]]:
            if key[1] <= lines[1][0][key[0]]:
                if key[1] >= lines[2][0][key[0]]:
                    if key[1] >= lines[3][0][key[0]]: 
                        map_space[key] = 0
    return map_space

def CreateOval(map_space):
    a = 40
    b = 20
    for key in map_space.keys():
        f = (((key[0]-149)**2)/(a**2))+(((key[1]-99)**2)/(b**2))-1
        if f <= 0:
            map_space[key] = 0
    return map_space

def CreateCircle(map_space):
    r = 25
    for key in map_space.keys():
        f = ((key[0]-224)**2)+((key[1]-49)**2)-(r**2)
        if f <= 0:
            map_space[key] = 0
    return map_space

# Given a predefined map, convert to binary map to determine obstacle space (point robot radius = 0, obstacle clearance = 0)
def CreateMap():
    # Create map dictionary which holds coordinates as a tuple of ints and the pixel value of that coordinate location as an int
    map_keys = []
    for i in range(0, 199):
        for j in range(0, 300):
            map_keys.append((j, i))

    map_values = list(np.ones(300 * 200, dtype=int))
    map_space = dict(zip(map_keys, map_values))

    map_space = CreateRect(map_space)
    map_space = CreateRhombus(map_space)
    map_space = CreatePoly1(map_space)
    map_space = CreatePoly2(map_space)
    map_space = CreatePoly3(map_space)
    map_space = CreateOval(map_space)
    map_space = CreateCircle(map_space)

    return map_space

# Obtaining Input from user : Start Point and Goal Point
# Check feasibility of  User Input : For start or goal nodes in obstacle
# space or outside range of binary map, inform user to redefine points try again
def GetStartGoal(map_space):
    start_goal_bad = True

    while (start_goal_bad):
        start_list = []
        goal_list = []
        while ((start_list == []) or (goal_list == []) or (len(start_list) > 1) or (len(goal_list) > 1)):
            start_input = input("Enter the starting point of the robot within the boundaries of the map (300 by 200) in the form, x, y: ")
            goal_input = input("Enter the goal point of the robot within the boundaries of the map (300 by 200) in the form, x, y: ")
            start_list = re.findall(r"[0-2]?[0-9]?[0-9], [0-1]?[0-9]?[0-9]", start_input)
            goal_list = re.findall(r"[0-2]?[0-9]?[0-9], [0-1]?[0-9]?[0-9]", goal_input)

        start = tuple(map(int, start_list[0].split(', ')))
        goal = tuple(map(int, goal_list[0].split(', ')))
        if ((0 < start[0] < 300) and (0 < goal[0] < 300)):
            if ((0 < start[1] < 200) and (0 < goal[1] < 200)):
                if (map_space[start] == 1):
                    if (map_space[goal] == 1):
                        if (map_space[goal] == 0):
                            print("goal position either outside of map boundary or is occupied by obstacle...")
                        if (map_space[start] == 0):
                            print("start position either outside of map boundary or is occupied by obstacle...")
                        start_goal_bad = False
    return start, goal

# Implement Djikstra's Algorithm
# Implementing Backtracking (once goal node is achieved)

class PointNode:
    def __init__(self, Node_State_i=[], Node_Cost_i=0, Node_Parent_i=0):
        self.Node_State_i = Node_State_i
        self.Node_Cost_i = Node_Cost_i
        self.Node_Parent_i = Node_Parent_i

#Implementing functions to add and get Nodes from the PointNode priority queue
def addNewNode(point_Node, newNode_cost, newNode):
    hpq.heappush(point_Node.Node_State_i, (newNode_cost, newNode))

def getNode(currentNode):
    node_removed = hpq.heappop(currentNode.Node_State_i)
    node = node_removed[1]
    cost = node_removed[0]
    return node, cost

def getCost(current_node_cost, new_node_move):
    #Implementing a data structure (priority queue) to store Nodes
    ListOfNeighborsMoves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1),
                            (1, -1), (-1, -1)]
    ListOfNeighborsMovesCost = [1, 1, 1, 1, 1.4, 1.4, 1.4, 1.4]
    index = ListOfNeighborsMoves.index(new_node_move)
    new_node_cost = current_node_cost + ListOfNeighborsMovesCost[index]
    return new_node_cost

# ############################################
#Testing adding and removing Nodes from PointNode:

# def priorityQueueTest():
#     startNode = [1, 2]
#     ListOfNodes = PointNode()
#     print("Empty list = ", ListOfNodes.Node_State_i)
#     addNewNode(ListOfNodes, 13, startNode)
#     print("List after adding startNode = ", ListOfNodes.Node_State_i)
#     newNode1 = [13, 4]
#     addNewNode(ListOfNodes, 12, newNode1)
#     print("List after adding newNode1 = ", ListOfNodes.Node_State_i)
#     newNode2 = [5, 6]
#     addNewNode(ListOfNodes, 16, newNode2)
#     print("List after adding newNode2 = ", ListOfNodes.Node_State_i)
#     newNode3 = [12, 3]
#     addNewNode(ListOfNodes, 5, newNode3)
#     print("List after adding newNode3 = ", ListOfNodes.Node_State_i)
#     getNode(ListOfNodes)
#     print(ListOfNodes.Node_State_i)
#     getNode(ListOfNodes)
#     print(ListOfNodes.Node_State_i)

# ############################################

# Implementing Djikstra's Algorithm
def applyingDijkstraAlgorithm(start_node, goal_node):
    #Implementing a data structure (priority queue) to store Nodes
    ListOfNeighborsMoves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1),
                            (1, -1), (-1, -1)]
    ListOfNeighborsMovesCost = [1, 1, 1, 1, 1.4, 1.4, 1.4, 1.4]
    exploredNodesPath = {}  # Contains list of explored nodes
    exploredNodesCost = {}  # Contains list of explored nodes cost
    exploredNodesPath[start_node] = 0
    exploredNodesCost[start_node] = 0
    ListOfNodes = PointNode()
    addNewNode(ListOfNodes, 0, start_node)
    print("Explored Node Cost ", exploredNodesCost)
    print("List of Nodes ", ListOfNodes.Node_State_i)
    while len(ListOfNodes.Node_State_i) > 0:
        currentNode, currentNodeCost = getNode(ListOfNodes)
        print("Current Node ", currentNode)
        print("Current Node Cost = ", currentNodeCost)
        if currentNode == goal_node:
            break
        for newNodeMove in ListOfNeighborsMoves:
            newNode = (currentNode[0] + newNodeMove[0],
                       currentNode[1] + newNodeMove[1])
            if newNode[0] < 0 or newNode[
                    1] < 0:  # Need to add condition for x move greater than 300 and y move greater than 200
                print("New node has negative coordinates, skipping it..",
                      newNode)
                continue
            print("New Node = ", newNode)
            newNodeCost = round(getCost(currentNodeCost, newNodeMove), 3)
            print("New Node cost = ", newNodeCost)
            if newNode not in exploredNodesCost or newNodeCost < exploredNodesCost[
                    newNode]:
                exploredNodesCost[newNode] = newNodeCost
                addNewNode(ListOfNodes, newNodeCost, newNode)
                exploredNodesPath[newNode] = currentNode
    return exploredNodesPath


#Implementing backtracking algorithm between start node and goal node and storing results on list pathlist[]
def backtrackingStartGoalPath(start, goal, explored_path):
    pathlist = []
    goalpath = goal
    pathlist.append(goal)
    while goalpath != start:
        pathlist.append(explored_path[goalpath])
        goalpath = explored_path[goalpath]
    pathlist.reverse()
    return pathlist

# Using pygame implement animation of map exploration and display optimal path

# accepts optimal path list, visited node list, and map_space as parameters
def Visualize(path, visited, map_space):
    pyg.display.init()
    map_screen = pyg.display.set_mode((300, 200))
    while (True):
        b1 = False
        b2 = False
        b3 = False
        for event in pyg.event.get():
            (b1, b2, b3) = pyg.mouse.get_pressed()
            if (event.type == QUIT):
                pyg.quit()
                sys.exit()
        if b1 or b2 or b3:
            map_screen.fill((255, 255, 255))
            pyg.display.set_caption("Map")
            for key in map_space.keys():
                if map_space[key] == 0:
                    map_screen.set_at(key, (0, 0, 0))
                else:
                    map_screen.set_at(key, (255, 255, 255))
            for node in visited:
                map_screen.set_at(node, (0, 0, 255))
                for event in pyg.event.get():
                    if (event.type == QUIT):
                        pyg.quit()
                        sys.exit()
                pyg.time.delay(100)
                pyg.display.update()
            for node in path:
                map_screen.set_at(node, (0, 255, 0))
                pyg.display.update()
            

#main function which calls all subfunctions necessary to solve the maze with Dijkstra's algorithm
def main():
    map_space = CreateMap()
    start, goal = GetStartGoal(map_space)
    visited = applyingDijkstraAlgorithm(start,goal)
    path = backtrackingStartGoalPath(start, goal, visited)
    Visualize(path, visited, map_space)

main()