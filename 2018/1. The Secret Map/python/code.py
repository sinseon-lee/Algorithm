# Decoding Function
def decoder(n, arr1, arr2):
    arr1Converted = []
    arr2Converted = []
    
    # convert number to binary array
    for i in arr1:
        arr1Converted.append(converter(i, n))
    for i in arr2:
        arr2Converted.append(converter(i, n))

    # check there is a wall or not using OR(|) command
    array = []
    for i in range(n):
        string = ""

        for j in range(n):
            element = arr1Converted[i][j] | arr2Converted[i][j]
            if (element == 0):
                string += " "
            else:
                string += "#"

        array.append(string)

    return array

# Get string information in the form of binary array
def converter(num, n):
    array = []

    while (num != 0):
        if (num%2 == 0):
            array = [0] + array
        else:
            array = [1] + array
    
        num /= 2

    if (len(array) != n):
        for i in range(n - len(array)):
            array = [0] + array

    return array

# Test 1
n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]

print(decoder(n, arr1, arr2))

# Test 2
n = 6
arr1 = [46, 33, 33 ,22, 31, 50]
arr2 = [27 ,56, 19, 14, 14, 10]

print(decoder(n, arr1, arr2))
