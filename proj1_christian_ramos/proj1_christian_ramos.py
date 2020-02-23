import copy
import time

# Class Node that contains information about each Node
class PuzzleNode:
    def __init__(self, Node_State_i= [],Node_State_i_Int= 0, Node_Index_i=1,Parent_Node_Index_i=0,BlankTileIndex=(0,0)):
        self.Node_State_i = Node_State_i
        self.Node_State_i_Int = Node_State_i_Int
        self.Node_Index_i = Node_Index_i
        self.Parent_Node_Index_i = Parent_Node_Index_i
        self.BlankTileIndex = BlankTileIndex

# Convert 2D array to 1D array:
def conv2Dto1D(arr2D):
    arr1D = []
    for i in range(3):
        for j in range(3):
            arr1D.append(arr2D[i][j])
    return arr1D

# Check if input puzzle is solvable:
def isPuzzleSolvable(start_arr2D, goal_arr2D):
    isSolvable  = False
    start_arr1D = conv2Dto1D(start_arr2D)
    goal_arr1D  = conv2Dto1D(goal_arr2D)
    start_invCount = 0
    goal_invCount = 0
    for i in range(8):
        for j in range(i+1,9):
            if(start_arr1D[j]!=0 and start_arr1D[i] > start_arr1D[j]):
                start_invCount +=1
    for i in range(8):
        for j in range(i+1,9):
            if(goal_arr1D[j]!=0 and goal_arr1D[i] > goal_arr1D[j]):
                goal_invCount +=1
    if((start_invCount%2==0 and goal_invCount%2==0)):
        print("Puzzle can be solved!!")
        isSolvable = True
    if((start_invCount%2!=0 and goal_invCount%2!=0)):
        print("Puzzle can be solved!!")
        isSolvable = True
    return isSolvable
	
# Check if Goal Node has been found:
def verifyGoalNode(currentNodePuzzle, newNodePuzzle):
    intCurrPuzzle = puzzleNodeToInt(currentNodePuzzle)
    intNewPuzzle = puzzleNodeToInt(newNodePuzzle)
    if intCurrPuzzle == intNewPuzzle:
        print("Target Goal Node Achieved...")
        return True
    else:
        return False

# Implementing BlankTileLocation function to localize index of 0 value in 3x3 Matrix
def BlankTileLocation(CurrentNode):
    for (index_i,row_val) in enumerate(CurrentNode.Node_State_i):
        for (index_j,col_val) in enumerate(row_val): 
            if col_val == 0:
                row = index_i
                column = index_j
                CurrentNode.BlankTileIndex = (row,column)
                break
    return (row, column)

# Function to add a Node (Optimizing by converting array of elements to a single integer) to Matrix List:
def AddNodeInt(CurrentNode):
    global matrix_Idx
    global Matrix_8puzzle_Nodes
    intPuzzle = puzzleNodeToInt(CurrentNode)
    CurrentNode.State_Node_i_Int = intPuzzle
    NonRepeatedPuzzle = True
    for i in Matrix_8puzzle_Nodes:
        if (Matrix_8puzzle_Nodes[i].State_Node_i_Int == CurrentNode.State_Node_i_Int):
            NonRepeatedPuzzle = False
            break
    if NonRepeatedPuzzle:
        CurrentNode.Node_Index_i = matrix_Idx
        Matrix_8puzzle_Nodes[matrix_Idx] = CurrentNode
        matrix_Idx = matrix_Idx + 1

# Converting a 2D array Puzzle to a single integer for optimization purposes
def puzzleNodeToInt(Node):
    array1D = conv2Dto1D(Node.Node_State_i)
    exponent = 8
    intPuzzle = 0
    for i in array1D:
        intPuzzle = intPuzzle + (i * 10**exponent)
        exponent = exponent - 1 
    return intPuzzle
	
# Function that moves blank tile to left and saves new node to matrix list:
def ActionMoveLeft(currentNode, goalNode):

    isGoalAchieved = False
    
    # Making a new independent copy using deepcopy()
    New_Node = copy.deepcopy(currentNode)

    #Locating Blank tile index position in puzzle
    row, column = currentNode.BlankTileIndex

    if column > 0:

        #Swapping blank tile value to left neighbor tile
        temp = New_Node.Node_State_i[row][column]
        New_Node.Node_State_i[row][column] = New_Node.Node_State_i[row][column-1]
        New_Node.Node_State_i[row][column-1] = temp
        
        # Updating Parent Node Index of newly created Node
        New_Node.Parent_Node_Index_i = currentNode.Node_Index_i 
        
        #Adding Node to Matrix_8puzzle_Nodes Dictionary
        AddNodeInt(New_Node)
        
        #Check if goal has been achieved
        isGoalAchieved = verifyGoalNode(New_Node,goalNode)

    return isGoalAchieved

# Function that moves blank tile Up and saves new node to matrix list:
def ActionMoveUp(currentNode, goalNode):
    
    isGoalAchieved = False
    
    # Making a new independent copy using deepcopy()
    New_Node = copy.deepcopy(currentNode)

    #Locating Blank tile index position in puzzle
    row, column = currentNode.BlankTileIndex
        
    if row > 0:
    
        #Swapping blank tile value to above neighbor tile
        temp = New_Node.Node_State_i[row][column]
        New_Node.Node_State_i[row][column] = New_Node.Node_State_i[row-1][column]
        New_Node.Node_State_i[row-1][column] = temp
        
        # Updating Parent Node Index of newly created Node
        New_Node.Parent_Node_Index_i = currentNode.Node_Index_i 

        #Adding Node to Matrix_8puzzle_Nodes Dictionary
        AddNodeInt(New_Node)

        #Check if goal has been achieved
        isGoalAchieved = verifyGoalNode(New_Node,goalNode)
        
    return isGoalAchieved

# Function that moves blank tile to right and saves new node to matrix list:
def ActionMoveRight(currentNode, goalNode):

    isGoalAchieved = False
    
    # Making a new independent copy using deepcopy()
    New_Node = copy.deepcopy(currentNode)

    #Locating Blank tile index position in puzzle
    row, column = currentNode.BlankTileIndex
    
    if column < 2:
        
        #Swapping blank tile value to right neighbor tile
        temp = New_Node.Node_State_i[row][column]
        New_Node.Node_State_i[row][column] = New_Node.Node_State_i[row][column+1]
        New_Node.Node_State_i[row][column+1] = temp

        # Updating Parent Node Index of newly created Node
        New_Node.Parent_Node_Index_i = currentNode.Node_Index_i 
        
        #Adding Node to Matrix_8puzzle_Nodes Dictionary
        AddNodeInt(New_Node)

        #Check if goal has been achieved
        isGoalAchieved = verifyGoalNode(New_Node,goalNode)
        
    return isGoalAchieved
	
# Function that moves blank tile Down and saves new node to matrix list:
def ActionMoveDown(currentNode, goalNode):
    
    isGoalAchieved = False
    
    # Making a new independent copy using deepcopy()
    New_Node = copy.deepcopy(currentNode)    

    #Locating Blank tile index position in puzzle
    row, column = currentNode.BlankTileIndex
        
    if row < 2:
        
        #Swapping blank tile value to below neighbor tile
        temp = New_Node.Node_State_i[row][column]
        New_Node.Node_State_i[row][column] = New_Node.Node_State_i[row+1][column]
        New_Node.Node_State_i[row+1][column] = temp
        
        # Updating Parent Node Index of newly created Node
        New_Node.Parent_Node_Index_i = currentNode.Node_Index_i 
        
        #Adding Node to Matrix_8puzzle_Nodes Dictionary
        AddNodeInt(New_Node)

        #Check if goal has been achieved
        isGoalAchieved = verifyGoalNode(New_Node,goalNode)
        
    return isGoalAchieved
	
# Function that allows move in all directions except left:
def NoMoveLeft(currentNode, goalNode):
    if ActionMoveUp(currentNode,goalNode): return True
    if ActionMoveRight(currentNode,goalNode): return True
    if ActionMoveDown(currentNode,goalNode): return True
	
# Function that allows move in all directions except Up:
def NoMoveUp(currentNode, goalNode):
    if ActionMoveLeft(currentNode,goalNode): return True
    if ActionMoveRight(currentNode,goalNode): return True
    if ActionMoveDown(currentNode,goalNode): return True

# Function that allows move in all directions except Right:
def NoMoveRight(currentNode, goalNode):
    if ActionMoveLeft(currentNode,goalNode): return True
    if ActionMoveUp(currentNode,goalNode): return True
    if ActionMoveDown(currentNode,goalNode): return True
	
# Function that allows move in all directions except Down:
def NoMoveDown(currentNode, goalNode):
    if ActionMoveLeft(currentNode,goalNode): return True
    if ActionMoveUp(currentNode,goalNode): return True
    if ActionMoveRight(currentNode,goalNode): return True
	
# Function to backtrack solution from Start Node to Goal Node
def backTrackingNodePath(Matrix_8puzzle_Nodes,startNode):
    NodePath = []
    goal_index = len(Matrix_8puzzle_Nodes)
    Parent_Idx = Matrix_8puzzle_Nodes[goal_index].Parent_Node_Index_i
    NodePath.append(str(Matrix_8puzzle_Nodes[goal_index].Node_State_i))    
    while Parent_Idx != 0:
        NodePath.append(str(Matrix_8puzzle_Nodes[Parent_Idx].Node_State_i))
        Parent_Idx = Matrix_8puzzle_Nodes[Parent_Idx].Parent_Node_Index_i
    NodePath.reverse()
    return NodePath
	
# Function that saves Puzzle Nodes Path to text file nodePath.txt:
def savePuzzleToNodePathFile(NodePathList):
    outFile = open("nodePath.txt","w")
    for i in NodePathList:
        strNodePathList = i.replace('[','').replace(']','')        
        strNPL = strNodePathList.replace(',', '').replace(' ','')
        columnFormatNodePath = strNPL[0] + " " + strNPL[3] + " " + strNPL[6] + " " + strNPL[1] + " " + strNPL[4] + " " + strNPL[7] + " " + strNPL[2] + " " + strNPL[5] + " " + strNPL[8]
        outFile.writelines(columnFormatNodePath)
    outFile.close()

# Function that saves explored puzzle nodes to Nodes.txt:
def savePuzzleToNodesFile(Matrix_8puzzle_Nodes):
    outFile = open("Nodes.txt","w")
    for i in Matrix_8puzzle_Nodes:
        Matpuzzle = str(Matrix_8puzzle_Nodes[i].Node_State_i).replace('[','').replace(']','')
        Mat8 = Matpuzzle.replace(',', '').replace(' ','')
        formattedMatrix8 = Mat8[0] + " " + Mat8[3] + " " + Mat8[6] + " " + Mat8[1] + " " + Mat8[4] + " " + Mat8[7] + " " + Mat8[2] + " " + Mat8[5] + " " + Mat8[8]
        outFile.writelines(formattedMatrix8)
        outFile.writelines('\n')
    outFile.close()

# Function that saves puzzle Nodes Indexes and their Parent Indexes to NodesInfo.txt:	
def savePuzzleToNodesInfoFile(Matrix_8puzzle_Nodes):
    outFile = open("NodesInfo.txt","w")
    for i in Matrix_8puzzle_Nodes:
        strMat8Puzzle = str(Matrix_8puzzle_Nodes[i].Node_Index_i) + " " + str(Matrix_8puzzle_Nodes[i].Parent_Node_Index_i) + " 0"
        outFile.writelines(strMat8Puzzle)
        outFile.writelines('\n')
    outFile.close()
	
######## MAIN PROGRAM ########
t = time.time()

Matrix_8puzzle_Nodes = {}
matrix_Idx = 1              # Index of Matrix_8puzzle_Nodes

#Entering Initial 8-Puzzle Matrix and desired Goal Puzzle:
Start_Node = PuzzleNode([[2, 8, 3], [1, 6, 4], [7, 0, 5]])    
Goal_Node =  PuzzleNode([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

isSolvable = isPuzzleSolvable(Start_Node.Node_State_i, Goal_Node.Node_State_i)

if (isSolvable):
    #Adding Initial Node to 8-Puzzle Matrix
    AddNodeInt(Start_Node)

    Current_Node = Matrix_8puzzle_Nodes[1]
    BlankTileLocation(Current_Node)

    ActionMoveLeft(Current_Node,Goal_Node)
    ActionMoveUp(Current_Node,Goal_Node)
    ActionMoveRight(Current_Node,Goal_Node)
    ActionMoveDown(Current_Node,Goal_Node)
    
    for i in range(2,200000):
        
        Current_Node = Matrix_8puzzle_Nodes[i]
        
        curr_row, curr_column = BlankTileLocation(Current_Node)

        curr_node_parent_index = Current_Node.Parent_Node_Index_i

        prev_row, prev_column = BlankTileLocation(Matrix_8puzzle_Nodes[curr_node_parent_index])
        
        if prev_column > curr_column:
            if NoMoveRight(Current_Node, Goal_Node): break
            
        elif prev_column < curr_column:
            if NoMoveLeft(Current_Node, Goal_Node): break

        elif (prev_column == curr_column) and (prev_row > curr_row):
            if NoMoveDown(Current_Node, Goal_Node): break

        elif (prev_column == curr_column) and (prev_row < curr_row):
            if NoMoveUp(Current_Node, Goal_Node): break
            
        elif prev_row > curr_row:
            if NoMoveDown(Current_Node, Goal_Node): break

        elif prev_row < curr_row:
            if NoMoveUp(Current_Node, Goal_Node): break
            
        elif prev_row == curr_row and prev_column > curr_column:
            if NoMoveRight(Current_Node, Goal_Node): break

        elif prev_row == curr_row and prev_column < curr_column:
            if NoMoveLeft(Current_Node, Goal_Node): break

    NodePathList = backTrackingNodePath(Matrix_8puzzle_Nodes, Start_Node)
    
    savePuzzleToNodePathFile(NodePathList)
    savePuzzleToNodesFile(Matrix_8puzzle_Nodes)
    savePuzzleToNodesInfoFile(Matrix_8puzzle_Nodes)
    
    print("Program is over...")
    
else:
    print("Input Puzzle has no solution, program is terminating ...")
	
print("8-Puzzle Program Time elapsed",time.time()-t)
