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

def CreateRect(map_space, clearance, radius):
    lines = []
    corr_line1_x = (clearance + radius)*math.cos(30*math.pi/180)
    corr_line1_y = (clearance + radius)*math.sin(30*math.pi/180)
    corr_line2_x = (clearance + radius)*math.sin(30*math.pi/180)
    corr_line2_y = (clearance + radius)*math.cos(30*math.pi/180)
    corr_line3_x = (clearance + radius)*math.cos(30*math.pi/180)
    corr_line3_y = (clearance + radius)*math.sin(30*math.pi/180)
    corr_line4_x = (clearance + radius)*math.sin(30*math.pi/180)
    corr_line4_y = (clearance + radius)*math.cos(59*math.pi/180)
    rect_coords = [(38-corr_line1_x, 126-corr_line1_y),
                   (29-corr_line1_x, 131-corr_line1_y),
                   (29-corr_line2_x, 131+corr_line2_y),
                   (94-corr_line2_x, 169+corr_line2_y),
                   (94+corr_line3_x, 169+corr_line3_y),
                   (103+corr_line3_x, 164+corr_line3_y),
                   (103+corr_line4_x, 164-corr_line4_y),
                   (38+corr_line4_x, 126-corr_line4_y)]
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

def CreateRhombus(map_space, clearance, radius):   
    lines = []
    corr_x = (clearance + radius)*math.sin(59*math.pi/180)
    corr_y = (clearance + radius)*math.cos(59*math.pi/180)
    #rhomb_coords = [(199, 174), (224, 159), (249, 174), (224, 189)]
    rhomb_coords = [(224-corr_x, 159-corr_y),
                    (199-corr_x, 174-corr_y),
                    (199-corr_x, 174+corr_y),
                    (224-corr_x, 189+corr_y),
                    (224+corr_x, 189+corr_y),
                    (249+corr_x, 174+corr_y),
                    (249+corr_x, 174-corr_y),
                    (224+corr_x, 159-corr_y)]
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

def CreatePoly1(map_space, clearance, radius):   
    lines = []
    #poly1_coords = [(22.5, 50), (50, 50), (20, 80)]
    corr_line1_x = (clearance+radius)*math.cos(4.397*math.pi/180)
    corr_line1_y = (clearance+radius)*math.sin(4.397*math.pi/180)
    corr_line2_x = (clearance+radius)*math.sin(49.764*math.pi/180)
    corr_line2_y = (clearance+radius)*math.cos(49.764*math.pi/180)
    
    poly1_coords = [(22.5-corr_line1_x, 50-corr_line1_y),
                    (20-corr_line1_x, 80-corr_line1_y),
                    (20+corr_line2_x, 80+corr_line2_y),
                    (50+corr_line2_x, 50+corr_line2_y),
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

def CreatePoly2(map_space, clearance, radius):   
    lines = []
    #poly2_coords = (50, 50), (75, 80), (100, 50)
    corr_line1_x = (clearance+radius)*math.sin(50.19*math.pi/180)
    corr_line1_y = (clearance+radius)*math.cos(50.19*math.pi/180)
    corr2_x = (clearance+radius)*math.cos(50.19*math.pi/180)
    corr2_y = (clearance+radius)*math.sin(50.19*math.pi/180)
    corr3_x = (clearance+radius)*math.sin(50.19*math.pi/180)
    corr3_y = (clearance+radius)*math.cos(50.19*math.pi/180)
    
    poly1_coords = [(50-corr_line1_x, 50+corr_line1_y),
                    (75-corr_line1_x, 80+corr_line1_y),
                    (75+corr2_x, 80+corr2_y),
                    (100+corr3_x, 50+corr3_y),
                    (100, 50),
                    (50, 50)]
    for n in range(0, len(poly1_coords), 2):
        m, b= SolveLine(poly1_coords[n], poly1_coords[n + 1])
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

def CreatePoly3(map_space, clearance, radius):   
    lines = []
    #poly3_coords = [(25, 15), (22.5, 50), (100, 50), (75, 15)]
    corr_line1_x = (clearance+radius)*math.cos(4.397*math.pi/180)
    corr_line1_y = (clearance+radius)*math.sin(4.397*math.pi/180)
    corr_line3_x = (clearance+radius)*math.cos(35.5376*math.pi/180)
    corr_line3_y = (clearance+radius)*math.sin(35.5376*math.pi/180)
    corr_line4_y = clearance+radius
    
    poly1_coords = [(25-corr_line1_x, 15-corr_line1_y),
                    (22.5-corr_line1_x, 50-corr_line1_y),
                    (22.5, 50),
                    (100, 50),
                    (100+corr_line3_x, 50-corr_line3_y),
                    (75+corr_line3_x, 15-corr_line3_y),
                    (75, 15-corr_line4_y),
                    (25, 15-corr_line4_y)]
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
                    if key[1] >= lines[3][0][key[0]]: 
                        map_space[key] = 0
    return map_space

def CreateOval(map_space, clearance, radius):
    a = 40 + clearance + radius
    b = 20 + clearance + radius
    for key in map_space.keys():
        f = (((key[0]-149)**2)/(a**2))+(((key[1]-99)**2)/(b**2))-1
        if f <= 0:
            map_space[key] = 0
    return map_space

def CreateCircle(map_space, clearance, radius):
    r = 25 + clearance + radius
    for key in map_space.keys():
        f = ((key[0]-224)**2)+((key[1]-49)**2)-(r**2)
        if f <= 0:
            map_space[key] = 0
    return map_space

# Given a predefined map, convert to binary map to determine obstacle space (point robot radius = 0, obstacle clearance = 0)
def CreateMap(clearance, radius):
    # Create map dictionary which holds coordinates as a tuple of ints and the pixel value of that coordinate location as an int
    map_keys = []
    for i in range(0, 199):
        for j in range(0, 300):
            map_keys.append((j, i))

    map_values = list(np.ones(300 * 200, dtype=int))
    map_space = dict(zip(map_keys, map_values))
    map_space = CreateRect(map_space, clearance, radius)
    map_space = CreateRhombus(map_space, clearance, radius)
    map_space = CreatePoly1(map_space, clearance, radius)
    map_space = CreatePoly2(map_space, clearance, radius)
    map_space = CreatePoly3(map_space, clearance, radius)
    map_space = CreateOval(map_space, clearance, radius)
    map_space = CreateCircle(map_space, clearance, radius)

    return map_space

def GetClearanceRadius():
    rc_bad = True
    radius_list = []
    clearance_list = []
    while ((radius_list == []) or (clearance_list == []) or (len(radius_list) > 1) or (len(clearance_list) > 1)):
        radius_input = input("Enter the radius of the robot as an integer: ")
        clearance_input = input("Enter the clearance of the robot as an integer: ")
        radius_list = re.findall(r"[0-9]?[0-9]", radius_input)
        clearance_list = re.findall(r"[0-9]?[0-9]", clearance_input)
    radius = int(radius_list[0])
    clearance = int(clearance_list[0])
    return clearance, radius

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


def priorityQueueTest():
    startNode = [1, 2]
    ListOfNodes = PointNode()
    print("Empty list = ", ListOfNodes.Node_State_i)
    addNewNode(ListOfNodes, 13, startNode)
    print("List after adding startNode = ", ListOfNodes.Node_State_i)
    newNode1 = [13, 4]
    addNewNode(ListOfNodes, 12, newNode1)
    print("List after adding newNode1 = ", ListOfNodes.Node_State_i)
    newNode2 = [5, 6]
    addNewNode(ListOfNodes, 16, newNode2)
    print("List after adding newNode2 = ", ListOfNodes.Node_State_i)
    newNode3 = [12, 3]
    addNewNode(ListOfNodes, 5, newNode3)
    print("List after adding newNode3 = ", ListOfNodes.Node_State_i)
    getNode(ListOfNodes)
    print(ListOfNodes.Node_State_i)
    getNode(ListOfNodes)
    print(ListOfNodes.Node_State_i)


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
        for event in pyg.event.get():
            (b1, b2, b3) = pyg.mouse.get_pressed()
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
                pyg.time.delay(250)
                pyg.display.update()
            for node in path:
                map_screen.set_at(node, (0, 255, 0))
                pyg.display.update()


#main function which calls all subfunctions necessary to solve the maze with Dijkstra's algorithm
def main():
    clearance, radius = GetClearanceRadius()
    map_space = CreateMap(clearance, radius)
    start, goal = GetStartGoal(map_space)
    visited = applyingDijkstraAlgorithm(start,goal)
    path = backtrackingStartGoalPath(start, goal, visited)
    Visualize(path, visited, map_space)


main()