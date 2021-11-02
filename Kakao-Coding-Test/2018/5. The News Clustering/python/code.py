# get the Jaccard Similarity of give two strings
def similarity(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()

    alphabetList = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

    set1 = []
    set2 = []

    # make the multisets of each strings
    for i in range(len(str1) - 1):
        if (str1[0] in alphabetList and str1[1] in alphabetList):
            set1.append(str1[:2])
        str1 = str1[1:]
    for i in range(len(str2) -1):
        if (str2[0] in alphabetList and str2[1] in alphabetList):
            set2.append(str2[:2])
        str2 = str2[1:]
    
    intersection = []
    union = []
    # get the intersection and the union of two multisets
    while (len(set1) != 0):
        element = set1[0]

        if (element in set2):
            intersection.append(element)
            union.append(element)
            set1.remove(element)
            set2.remove(element)
        else:
            union.append(element)
            set1.remove(element)
    
    while (len(set2) !=0):
        element = set2[0]

        union.append(element)
        set2.remove(element)

    if (len(union) == 0):
        jaccardSimilarity = 1 * 65536
    else:
        jaccardSimilarity = int(len(intersection) / len(union) * 65536)

    return jaccardSimilarity

# Test 1
str1 = "FRANCE"
str2 = "french"
print(similarity(str1, str2))

# Test 2
str1 = "handshake"
str2 = "shake hands"
print(similarity(str1, str2))

# Test 3
str1 = "aa1+aa2"
str2 = "AAAA12"
print(similarity(str1, str2))

# Test 4
str1 = "E=M*C^2"
str2 = "e=m*c^2"
print(similarity(str1, str2))
