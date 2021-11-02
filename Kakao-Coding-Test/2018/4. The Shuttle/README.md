# 4. The Shuttle
Kakao offers free shuttle from the Pangyo station to the Kakao office. A large number of Kakao crews is going to work with this service.

For your convenience, the service info is below.
- The shuttle starts from *09:00*, *n* times, at *t*-minute intervals. Maximum m people are allowed for each shuttle.
- When the shuttle arrives, it takes crews including people who arrive at that time. Such as, the crew who arrives at *09:00* can take the *09:00* shuttle.

Con, who is very lazy, got the information of all crew's arrival time. Get the Con's optimal arrival time.

However, Con is so lazy that he lines up at the end of queue among crew's who arrive at the same time. Also, all crews go back home at *23:59*. 

## input
the number of the shuttle *n*, the interval of the shuttle *t*, maximum capacity of the shuttle *m*, the array of crew's arrival time *timetable*.

- 0 < *n* <= 10
- 0 < *t* <= 60
- 0 < *m* <= 45
- 1 <= the length of *timetable* <= 2000, and the format of the element is *HH:MM*.
- *HH:MM* is from *00:01* to *23:59*.

## output
- the latest arrival time for Con to go to the office. The format is *HH:MM*, and it would be from *00:00* to *23:59*.

## example
1.
- n = 1
- t = 1
- m = 5
- timetable = ["08:00", "08:01", "08:02", "08:03"]
- answer = "09:00"

2.
- n = 2
- t = 10
- m = 2
- timetable = ["09:10", "09:09", "08:00"]
- answer = "09:09"

3.
- n = 2
- t = 1
- m = 2
- timetable = ["09:00", "09:00", "09:00", "09:00"]
- answer = "08:59"

4.
- n = 1
- t = 1
- m = 5
- timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
- answer = "00:00"

5.
- n = 1
- t = 1
- m = 5
- timetable = ["23:59"]
- answer = "09:00"

6.
- n = 10
- t = 60
- m = 45
- timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
- answer = "18:00"
