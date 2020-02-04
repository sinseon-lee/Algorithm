# Count the removing blocks
def counter(m, n, board):
    # change string elements to array elements because it's easy to treat
    for i in range(len(board)):
        board[i] = strToArray(board[i])

    numToRemove = 0

    targets = getTargets(m, n, board)
    while (len(targets) != 0):
        numToRemove += len(targets)
        board = removeTargets(m, n, board, targets)
        targets = getTargets(m, n, board)

    return numToRemove

# "ABCDE" to ["A", "B", "C", "D", "E"]
def strToArray(str):
    array = []

    for i in range(len(str)):
        array.append(str[i])

    return array

# get the list of removing target elements' indices
def getTargets(m, n, board):
    targets = []

    for i in range(m - 1):
        for j in range(n - 1):
            element = board[i][j]

            if (element == ""):
                break
            
            if (board[i + 1][j] == element and board[i][j + 1] == element and board[i + 1][j + 1] == element):
                if ((i, j) not in targets):
                    targets.append((i, j))
                if ((i + 1, j) not in targets):
                    targets.append((i + 1, j))
                if ((i, j + 1) not in targets):
                    targets.append((i, j + 1))
                if ((i + 1, j + 1) not in targets):
                    targets.append((i + 1, j + 1))

    return targets

# Remove target elements and replace it
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
print(counter(m, n, board))

# Test 2
m = 6
n = 6
board = ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]
print(counter(m, n, board))
