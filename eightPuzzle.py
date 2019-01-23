
#for taking input from user
def inputState():
    mat = [[0,0,0],[0,0,0],[0,0,0]]
    a=0
    for i in range(0,3):
        for j in range(0,3):
            mat[i][j] = int(input("enter a state[{}][{}]:".format(i,j)))
            
    return mat

#for printing State
def showState(mat):
    for k in range(0,3):
        for l in range(0,3):
            print(mat[k][l],end=" ")
        print("")

#generates the sucessor having best h(n)
def generateSucessor(current,goal):
   x = getXPosOfZero(current)
   y = getYposOfZero(current)
   heurasticleft = 0
   heurasticright = 0
   heurastictop = 0
   heurasticbottom = 0
   #left successor
   if(x == 1 or x == 2):
        leftSuccessor = leftChild(current)
        heurasticleft = calculateHeuristic(leftSuccessor,goal)
   #right successor
   if(x == 0 or x == 1):
        rightSuccessor = rightChild(current)
        heurasticright = calculateHeuristic(rightSuccessor,goal)
   #top successor
   if(y == 0 or y == 1):
        topSuccessor = topChild(current)
        heurastictop = calculateHeuristic(topSuccessor,goal)
   #bottom successor
   if(y == 1 or y == 2):
        bottomSuccessor = bottomChild(current)
        heurasticbottom = calculateHeuristic(bottomSuccessor,goal)
   

   nextCurrentFlag = compareHeuristic(heurasticleft,heurasticright,heurastictop,heurasticbottom)

   if nextCurrentFlag == 1:
       return leftChild
   elif nextCurrentFlag == 2:
       return rightSuccessor
   elif nextCurrentFlag == 3:
       return topSuccessor
   else:
       return bottomSuccessor
    

#generate left child
def leftChild(current):
    for i in range(0,3):
        for j in range(0,3):
            if current[i][j] == 0:
                temp = current[i][j]
                current[i][j] = current[i-1][j]
                current[i-1][j] = temp
        
    return current

#generate right child
def rightChild(current):
    for i in range(0,2):
        for j in range(0,3):
            if current[i][j] == 0:
                temp = current[i][j]
                current[i][j] = current[i+1][j]
                current[i+1][j] = temp
    return current


#generate top child
def topChild(current):
    for i in range(0,3):
        for j in range(0,2):
            if current[i][j] == 0:
                temp = current[i][j]
                current[i][j] = current[i][j+1]
                current[i][j+1] = temp
    return current

#generate bottom child
def bottomChild(current):
    for i in range(0,3):
        for j in range(0,3):
            if current[i][j] == 0:
                temp = current[i][j]
                current[i][j] = current[i][j-1]
                current[i][j-1] = temp
    return current


#calculates the h(n)
def calculateHeuristic(current,goal):
     x = getXPosOfZero(current)
     y = getYPosOfZero(current)
     x1 = getXPosOfZero(goal)
     y1 = getYPosOfZero(goal)
     manhattan = math.abs(x1 - x) + math.abs(y1 - y)
     return manhattan
    

#calculates the x position of zero
def getXPosOfZero(current):
    #current = ast.literal_eval(current)
    b = 0
    for i in range(0,3):
        for j in range(0,3):
            if current[i][j] == b:
                return i
            else:
                continue
            
#caluclates the y position of zero
def getYposOfZero(current):
    a = 0
    for i in range(0,3):
        for j in range(0,3):
            if current[i][j] == a:
                return j
            else:
                continue

#find the best(greatest) heurastic value
def compareHeuristic(left,right,top,bottom):
    if left >= right & left >= top & left >= bottom:
        return 1
    elif right >= left & right >= top & right >= bottom:
        return 2
    elif top >= left & top >= right & top >= bottom:
        return 4
    else:
        return 5

# main function that runs first
def main():
    initial = [[0,0,0],[0,0,0],[0,0,0]]
    goal = [[0,0,0],[0,0,0],[0,0,0]]

    print("Input the initial state of eight puzzle")
    initial = inputState()
    print("Input the goal state of eight puzzle")
    goal = inputState()

    print("inital node")
    showState(initial)
    print("goal node")
    showState(goal)
    
    current = initial #at first initial state is current State
    #current = ast.literal_eval(current)
    
    if(goal == current):
        print(current)
        print("initial condtion is solution")
    else:
        sucessor = [[0,0,0],[0,0,0],[0,0,0]]
        sucessor = generateSucessor(current,goal)
        while calculateHeuristic(current,goal) <= calculateHeuristic(sucessor,goal):
            current = sucessor
            print(current)
            sucessor = generateSucessor(current,goal)
  
if __name__ == "__main__":
    main()
