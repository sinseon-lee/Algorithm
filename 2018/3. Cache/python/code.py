# Calculate the running time
def measurer(cacheSize, cities):
    time = 0
    cache = []

    # make all characters lower case as it's non-case-sensative
    for i in range(len(cities)):
        cities[i] = cities[i].lower()

    while (len(cities) != 0):
        city = cities[0]
        
        if (city in cache):
            time += 1
        else:
            time += 5

        cache.append(city)
        # to fix the cache size
        if (len(cache) > cacheSize):
            cache = cache[1:]

        cities = cities[1:]
        
    return time

# Test 1
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(measurer(cacheSize, cities))

# Test 2
cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(measurer(cacheSize, cities))

# Test 3
cacheSize = 2
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(measurer(cacheSize, cities))

# Test 4
cacheSize = 5
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
print(measurer(cacheSize, cities))

# Test 5
cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(measurer(cacheSize, cities))

# Test 6
cacheSize = 0
cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
print(measurer(cacheSize, cities))
