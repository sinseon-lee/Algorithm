# 3. Cache
Jay-Z, who is in the map development team, is developing the service which tells the popular restaurants around the city which users search.
Apeach, who is the coordinator of the testing part, measured the performance of logics before releasing the service. However, it took too much time to load data from the database.
Apeach started to rush Jay-Z. He's trying to apply the Database Cache, but he has no idea about the size of the cache.

To help Jay-Z, develop the running time for each cache size when the Database Cache is applied.


## input
- The size of the cache(*cacheSize*), and the array of cities' name(*cities*)
- *cacheSize* is integer, 0 <= *cacheSize* <=30
- *cities* is the array of strings which tells the name of cities, maximum 100,000.
- Each city name consists of English characters(no blank, number or any special symbols). It's non-case-sensitive. maximum 20 characters.

## output
- The total running time to deal with all cities in the array of cities' name in order.

## qualification
- Use *LRU*(Least Recently Used) Algorithm.
- The running time for *cache hit* is 1.
- The running time for *cache miss* is 5.

## example
1.
- cacheSize = 3
- cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
- Running time = 50

2.
- cacheSize = 3
- cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
- Running time = 21

3.
- cacheSize = 2
- cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
- Running time = 60

4.
- cacheSize = 5
- cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork", "Rome"]
- Running time = 52

5.
- cacheSize = 2
- cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
- Running time = 16

6.
- cacheSize = 0
- cities = ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]
- Running time = 25
