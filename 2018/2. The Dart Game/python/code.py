# Calculate the mark of the dart game
def calculator(dartResult):
    dartResult += " " # to avoid the case which has no option("*" or "#" in the last mark)
    markArray = []
    
    while(len(dartResult) != 0):
        # if there is no option in the last mark, break)
        if (dartResult == " "):
            break
        bonus = 0
        # find the index of the bonus("S", "D", or "T")
        arrayOfBonus = [dartResult.find("S"),
                        dartResult.find("D"),
                        dartResult.find("T")]

        # if there is no "S" in dartResult, arrayOfBonus[0] is -1
        for i in range(len(arrayOfBonus)):
            if (arrayOfBonus[i] == -1):
                arrayOfBonus[i] = 3

        indexOfBonus = min(arrayOfBonus)
        bonus = arrayOfBonus.index(indexOfBonus) + 1
        point = int(dartResult[:indexOfBonus]) ** bonus

        if (dartResult[indexOfBonus + 1] == "*" or
            dartResult[indexOfBonus + 1] == "#"):
            
            option = dartResult[indexOfBonus + 1]
            
            if (option == "*"):
                point *= 2
                if (len(markArray) > 0):
                    markArray[-1] *= 2
            else:
                point *= -1

            dartResult = dartResult[indexOfBonus + 2:]
        else:
            dartResult = dartResult[indexOfBonus + 1:]

        markArray.append(point)

    return sum(markArray)

# Test 1
dartResult = "1S2D*3T"
print(calculator(dartResult))

# Test 2
dartResult = "1D2S#10S"
print(calculator(dartResult))

# Test 3
dartResult = "1D2S0T"
print(calculator(dartResult))

# Test 4
dartResult = "1S*2T*3S"
print(calculator(dartResult))

# Test 5
dartResult = "1D#2S*3S"
print(calculator(dartResult))

# Test 6
dartResult = "1T2D3D#"
print(calculator(dartResult))

# Test 7
dartResult = "1D2S3T*"
print(calculator(dartResult))
