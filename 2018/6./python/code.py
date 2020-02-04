
def counter(m, n, board):
    for i in range(len(board)):
        board[i] = strToArray(board[i])

    numToRemove = 0
    targets = getTargets(m, n, board)
    print("targets : ", targets)
    while (len(targets) != 0):
        numToRemove += len(targets)

        board = removeTargets(m, n, board, targets)
        print("board :", board)
        targets = getTargets(m, n, board)
        print("targets : ", targets)
        print("numToRemove : ", numToRemove)

def strToArray(str):
    array = []
    for i in range(len(str)):
        array.append(str[i])

    return array

def getTargets(m, n, board):
    targets = []

    for i in range(m - 1):
        for j in range(n - 1):
            element = board[i][j]
            if (element == ""):
                break
            
            if (board[i + 1][j] == element and board[i][j + 1] == element and board[i + 1][j + 1] == element):
                print("i, j : ", i, j)
                if ((i, j) not in targets):
                    targets.append((i, j))
                if ((i + 1, j) not in targets):
                    targets.append((i + 1, j))
                if ((i, j + 1) not in targets):
                    targets.append((i, j + 1))
                if ((i + 1, j + 1) not in targets):
                    targets.append((i + 1, j + 1))

    return targets

def removeTargets(m, n, board, targets):
    
    for i, j in targets:
        
        if (i == 0):
            board[i][j] == ""
        else:
            n = 0
            while(i - n != 0):
                board[i - n][j] = board[i - n - 1][j]
                n += 1
            board[i - n][j] = ""

    return board



# Test 1
m = 4
n = 5
board = ["CCBDE", "AAADE", "AAABF", "CCBBF"]
counter(m, n, board)

# Test 2
m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
counter(m, n, board)
