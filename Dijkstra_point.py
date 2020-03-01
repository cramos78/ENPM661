import pygame as pyg
import sys
import numpy as np
from pygame.locals import *
import math as m
import heapq as hpq


# Given a predefined map, convert to binary map to determine obstacle space (point robot radius = 0, obstacle clearance = 0)
def CreateMap():
    # Create map dictionary which holds coordinates as a tuple of ints and the pixel value of that coordinate location as an int
    map_keys = []

    map_screen = pyg.Surface((300, 200))
    map_screen.fill((255, 255, 255))
    pyg.draw.circle(map_screen, (0, 0, 0), (224, 50), 25)
    pyg.draw.polygon(map_screen, (0, 0, 0), [(30, 131), (39, 126), (104, 164),
                                             (95, 169)])
    pyg.draw.polygon(map_screen, (0, 0, 0), [(25, 14), (75, 14), (100, 49),
                                             (75, 79), (50, 49), (20, 79)])
    pyg.draw.ellipse(map_screen, (0, 0, 0), [109, 79, 80, 40])
    pyg.draw.polygon(map_screen, (0, 0, 0), [(199, 174), (224, 159),
                                             (249, 174), (224, 189)])
    map_array = pyg.surfarray.pixels3d(map_screen)
    map_space = {}
    for i in range(0, len(map_array[0])):
        for j in range(0, len(map_array)):
            map_space[(j, i)] = map_array[j, i, 0]

    return map_space


# Obtaining Input from user : Start Point and Goal Point
# Check feasibility of  User Input : For start or goal nodes in obstacle
# space or outside range of binary map, inform user to redefine points try again
def GetInput(map_space):
    input_bad = True
    while (input_bad):
        start_input = input(
            "Enter the starting point of the robot within the boundaries of the map (300 by 200) in the form, x, y: "
        )
        goal_input = input(
            "Enter the goal point of the robot within the boundaries of the map (300 by 200) in the form, x, y: "
        )
        start_string = ''
        goal_string = ''
        for element in start_input:
            if element.isnumeric():
                if start_string == '':
                    start_string = element
                else:
                    start_string = start_string + ', ' + element
        for element in goal_input:
            if element.isnumeric():
                if goal_string == '':
                    goal_string = element
                else:
                    goal_string = goal_string + ', ' + element
        start = tuple(map(int, start_string.split(', ')))
        goal = tuple(map(int, goal_string.split(', ')))
        if ((0 < start[0] < 300) and (0 < goal[0] < 300)):
            if ((0 < start[1] < 200) and (0 < goal[1] < 200)):
                if (map_space[start] == 255):
                    if (map_space[goal] == 255):
                        input_bad = False
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
    exploredNodesPath = {}                 # Contains list of explored nodes
    exploredNodesCost = {}                 # Contains list of explored nodes cost
    exploredNodesPath[start_node] = 0
    exploredNodesCost[start_node] = 0
    ListOfNodes = PointNode()
    addNewNode(ListOfNodes,0,start_node)
    print("Explored Node Cost ",exploredNodesCost)
    print("List of Nodes ",ListOfNodes.Node_State_i)
    while len(ListOfNodes.Node_State_i) > 0:
        currentNode, currentNodeCost= getNode(ListOfNodes)
        print("Current Node ",currentNode)
        print("Current Node Cost = ", currentNodeCost)
        if currentNode == goal_node:
            break
        for newNodeMove in ListOfNeighborsMoves:
            newNode = (currentNode[0] + newNodeMove[0],currentNode[1] + newNodeMove[1])
            if newNode[0] < 0 or newNode[1] < 0 :     # Need to add condition for x move greater than 300 and y move greater than 200
                print("New node has negative coordinates, skipping it..",newNode)
                continue
            print("New Node = ",newNode)
            newNodeCost = round(getCost(currentNodeCost,newNodeMove),3)
            print("New Node cost = ", newNodeCost)
            if newNode not in exploredNodesCost or newNodeCost < exploredNodesCost[newNode]:
                exploredNodesCost[newNode] = newNodeCost
                addNewNode(ListOfNodes,newNodeCost,newNode)
                exploredNodesPath[newNode] = currentNode
    return exploredNodesPath

#Implementing backtracking algorithm between start node and goal node and storing results on list pathlist[]
def backtrackingStartGoalPath(start,goal,explored_path):
    pathlist = []
    goalpath = goal
    pathlist.append(goal)
    while goalpath != start:
        pathlist.append(explored_path[goalpath])
        goalpath = explored_path[goalpath]
    pathlist.reverse()
    return pathlist

# Using pygame implement animation of map exploration and display optimal path


def Visualize(path, visited, map_space):
    pyg.display.init()
    map_screen = pyg.display.set_mode((300, 200))
    while (True):
        map_screen.fill((255, 255, 255))
        pyg.display.set_caption("Map")
        for key in map_space.keys():
            if map_space[key] == 0:
                map_screen.set_at(key, (0, 0, 0))
            else:
                map_screen.set_at(key, (255, 255, 255))
            for node in visited:
                map_screen.set_at(key, (0, 0, 255))
        for event in pyg.event.get():
            if (event.type == QUIT):
                pyg.quit()
                sys.exit()
            pyg.display.update()
    pass


#main function which calls all subfunctions necessary to solve the maze with Dijkstra's algorithm
def main():
    #Implementing a data structure (priority queue) to store Nodes
    ListOfNeighborsMoves = [(0, 1), (1, 0), (0, -1), (-1, 0), (-1, 1), (1, 1),
                            (1, -1), (-1, -1)]
    ListOfNeighborsMovesCost = [1, 1, 1, 1, 1.4, 1.4, 1.4, 1.4]
    #start_Node = (4,5)
    #goal_Node = (20,20)
    map_space = CreateMap()
    start, goal = GetInput(map_space)
    #path = applyingDijkstraAlgorithm(start_Node,goal_Node)
    path = 1
    visited = []
    for i in range(0, 100):
        visited.append((i, i))
    Visualize(path, visited, map_space)


main()