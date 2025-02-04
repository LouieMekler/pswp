n = 3
startingPlayer = 0
startingMatrix = [[-1 for x in range(n)] for y in range(n)]

positions = []
for y in range(n):
    for x in range(n):
        positions.append([x,y])


def full(mat):
    for y in mat:
        for x in y:
            if x == -1:
                return False
    return True

def det(mat):
    if len(mat) == 1:
        return mat[0][0]
    
    if len(mat) == 2:
        return mat[0][0] * mat[1][1] - mat[0][1] * mat[1][0]
    
    d = 0
    for col in range(len(mat)):
        sub_mat = [row[:col] + row[col+1:] for row in mat[1:]]
        cofactor = ((-1) ** col) * mat[0][col] * det(sub_mat)
        d += cofactor
    
    return d


def game(mat,player):
    if full(mat):
        return (det(mat)==0) == (player==0)

    for pos in positions:
        if mat[pos[0]][pos[1]] == -1:
            next_mat = [[x for x in y] for y in mat]
            next_mat[pos[0]][pos[1]] = player
            if not game(next_mat,1-player):
                return True
            
    return False

if __name__ == "__main__":
    print(f"Player {startingPlayer} goes first on this board")
    for y in startingMatrix:
        print("[",end="")
        for x in y[:-1:]:
            if x == -1: print(" ",end=",")
            else: print(x,end=",")
        if y[-1] == -1: print(" ",end="]\n")
        else : print(y[-1],end="]\n")
            
            
    result = game(startingMatrix,startingPlayer)
    winner = startingPlayer if result else 1 - startingPlayer
    print(f"Player {winner} wins!")
