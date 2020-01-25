# Calculate the optimal time
def schedule(n, t, m, timetable):
    departureTimes = [540]

    # make a list of departure times
    for i in range(n - 1):
        departureTimes.append(departureTimes[-1] + t)
    # remember the last departure time for 
    lastDepartureTime = departureTimes[-1]

    # make HH:MM to minute(integer)
    for i in range(len(timetable)):
        timetable[i] = timeToInteger(timetable[i])
    
    timetable.sort()

    queues = []
    # make a list of the information of the crew's shuttle allocation 
    while (len(departureTimes) != 0 and len(timetable) != 0):
        departureTime = departureTimes[0]
        queue = []
        
        while (timetable[0] <= departureTime):
            if (len(queue) >= m):
                break
            
            queue.append(timetable[0])
            if (len(timetable) == 1):
                break
            timetable = timetable[1:]

        queues.append(queue)
        departureTimes = departureTimes[1:]

    # if the last shuttle is not full, optimal time is the last departure time
    if (len(queues[-1]) != m):
        optimalTime = lastDepartureTime
    # if the last shuttle is full, optimal time is the last crew's arrival time - 1
    else:
        optimalTime = queues[-1][-1] - 1

    return integerToTime(optimalTime)


# HH:MM(string) to minute(integer):
def timeToInteger(string):
    hour = int(string[0:2])
    minute = int(string[3:5])

    return hour * 60 + minute

# minute(integer to HH:MM)
def integerToTime(integer):
    hour = str(int(integer / 60))
    minute = str(integer % 60)
    
    time = hour + ":" + minute
    if (time[1] == ":"):
        time = "0" + time
    if (time[-2] == ":"):
        time = time[:-1] + "0" + time[-1]

    return time

# Test 1
n = 1
t = 1
m = 5
timetable = ["08:00", "08:01", "08:02", "08:03"]
print(schedule(n, t, m, timetable))

# Test 2
n = 2
t = 10
m = 2
timetable = ["09:10", "09:09", "08:00"]
print(schedule(n, t, m, timetable))

# Test 3
n = 2
t = 1
m = 2
timetable = ["09:00", "09:00", "09:00", "09:00"]
print(schedule(n, t, m, timetable))

# Test 4
n = 1
t = 1
m = 5
timetable = ["00:01", "00:01", "00:01", "00:01", "00:01"]
print(schedule(n, t, m, timetable))

# Test 5
n = 1
t = 1
m = 5
timetable = ["23:59"]
print(schedule(n, t, m, timetable))

# Test 6
n = 10
t = 60
m = 45
timetable = ["23:59","23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59", "23:59"]
print(schedule(n, t, m, timetable))
