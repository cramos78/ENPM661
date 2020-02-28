import pygame as pyg
import heapq as hpq

# Given a predefined map, convert to binary map to determine obstacle space (point robot radius = 0, obstacle clearance = 0)



# Obtaining Input from user : Start Point and Goal Point



# Check feasibility of  User Input : For start or goal nodes in obstacle space or outside range of binary map, inform user to redefine points try again


#Implementing a data structure (priority queue) to store Nodes
ListOfNeighborsMoves =       [(0,1),(1,0),(0,-1),(-1,0),(-1,1),(1,1),(1,-1),(-1,-1)]
ListOfNeighborsMovesCost = [   1  ,   1  ,    1   ,    1  ,  1.4  , 1.4 ,  1.4  ,  1.4   ]

class PointNode:
	def __init__(self, Node_State_i = [], Node_Cost_i = 0, Node_Parent_i = 0):
		self.Node_State_i = Node_State_i
		self.Node_Cost_i = Node_Cost_i
		self.Node_Parent_i = Node_Parent_i

#Implementing functions to add and get Nodes from the PointNode priority queue 
def addNewNode(point_Node,newNode_cost,newNode):
	hpq.heappush(point_Node.Node_State_i,(newNode_cost,newNode))
	
def getNode(currentNode):
	node_removed = hpq.heappop(currentNode.Node_State_i)
	node = node_removed[1]
	cost = node_removed[0]
	return node, cost
	
def getCost(current_node_cost, new_node_move):
	index = ListOfNeighborsMoves.index(new_node_move)
	new_node_cost =  current_node_cost + ListOfNeighborsMovesCost[index]
	return new_node_cost
# ############################################
#Testing adding and removing Nodes from PointNode:

def priorityQueueTest():
	startNode = [1,2]
	ListOfNodes = PointNode()
	print("Empty list = ",ListOfNodes.Node_State_i)
	addNewNode(ListOfNodes,13,startNode)
	print("List after adding startNode = ",ListOfNodes.Node_State_i)
	newNode1 = [13,4]
	addNewNode(ListOfNodes,12,newNode1)
	print("List after adding newNode1 = ",ListOfNodes.Node_State_i)
	newNode2 = [5,6]
	addNewNode(ListOfNodes,16,newNode2)
	print("List after adding newNode2 = ",ListOfNodes.Node_State_i)
	newNode3 = [12,3]
	addNewNode(ListOfNodes,5,newNode3)
	print("List after adding newNode3 = ",ListOfNodes.Node_State_i)

	getNode(ListOfNodes)
	print(ListOfNodes.Node_State_i)
	getNode(ListOfNodes)
	print(ListOfNodes.Node_State_i)

# ############################################
start_Node = (4,5)
goal_Node = (20,20)

# Implementing Djikstra's Algorithm
def applyingDijkstraAlgorithm(start_node, goal_node):
	exploredNodesPath = {}
	exploredNodesCost = {}
	exploredNodesPath[start_Node] = 0
	exploredNodesCost[start_Node] = 0
	ListOfNodes = PointNode()
	addNewNode(ListOfNodes,0,start_Node)
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
			print("New Node = ",newNode)
			newNodeCost = currentNodeCost + getCost(currentNodeCost,newNodeMove)
			print("New Cost =" , newNodeCost)
			if newNode not in exploredNodesCost or newNodeCost < exploredNodesCost[newNode]:
				exploredNodesCost[newNode] = newNodeCost
				addNewNode(ListOfNodes,newNodeCost,newNode)
				exploredNodesPath[newNode] = newNodeCost
	return exploredNodesPath	
		
		
	
applyingDijkstraAlgorithm(start_Node,goal_Node)
	


# Implementing Backtracking (once goal node is achieved) 



# Using pygame implement animation of optimal path generation








