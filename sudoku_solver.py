#initial board to be solved where 0 is a blank space on board 

board=[
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
    ]

def get_empty(boa):
    for i in range(len(boa)):
        for j in range(len(boa[0])):
            if boa[i][j]==0:
                return (i,j)  #returns row and column
    return None 

def viable(boa,number,pos):
    #see if number being inserted is not in the same column, row or square
    #checking row
    for i in range(len(boa[0])):
        if boa[pos[0]][i]==number and pos[1] != i:
            return False
    #checking column
    for i in range(len(boa)):
        if boa[i][pos[1]] ==number and pos[0] != 1:
            return False

    #checking square
    box_x=pos[1]//3
    box_y=pos[0]//3

    for i in range(box_y*3,box_y*3 + 3):
        for j in range(box_x*3,box_x*3 + 3):
            if boa[i][j]==number and (i,j) != pos:
                return False

    return True

def solve(boa):
    find=get_empty(boa)
    if not find:
        return True
    else:
        row,col = find

    for i in range(1,10):               #numbers 1-9 to be added
        if viable(boa, i, (row,col)):    #determine if number being added makes board valid
            boa[row][col]=i             #if valid is true then add number 

            if solve(boa):              #recursive call to solve again   
                return True

            boa[row][col]=0              #if solve not true replace last element because cant be correct       
    return False
            
def printboard(boa):
    for i in range(len(boa)):
        if i % 3 ==0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(boa[0])):
            if j%3 ==0 and j!=0:
                print(" | ", end="")

            if j ==8:
                print (boa[i][j])
            else:
                print(str(boa[i][j]) + " ", end="")
print("Inital board")
printboard(board)
solve(board)
print("")
print("Solved Board")
printboard(board)
