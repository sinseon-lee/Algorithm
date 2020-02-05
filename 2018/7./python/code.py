
def solution(lines):
    traffics = []

    for line in lines:
        
        
        completeTime = line.split(" ")[1]
        hour = float(completeTime.split(":")[0])
        minute = float(completeTime.split(":")[1])
        second = float(completeTime.split(":")[2])
        completeSecond = hour * 60 * 60 + minute * 60 + second

        interval = float(line.split(" ")[2][:-1])

        
        traffics.append((round(completeSecond + 0.001 - interval, 3), completeSecond))

    print(traffics)

    maxNumTraffic = 0
    for traffic in traffics:
        start = traffic[0]
        end = traffic[1]
        
        count = 0
        for traffic in traffics:
            if (round(start - 1 + 0.001, 3) <= traffic[1] and traffic[0] <= start):
                count += 1
        if (maxNumTraffic < count):
            maxNumTraffic = count

        count = 0
        for traffic in traffics:
            if (end <= traffic[1] and traffic[0] <= round(end + 1 - 0.001, 3)):
                count += 1
        if (maxNumTraffic < count):
            maxNumTraffic = count


    print(maxNumTraffic)
    return maxNumTraffic



# Test 1
lines = ["2016-09-15 01:00:04.001 2.0s", "2016-09-15 01:00:07.000 2s"]
solution(lines)

# Test 2
lines = ["2016-09-15 01:00:04.002 2.0s", "2016-09-15 01:00:07.000 2s"]
solution(lines)

# Test 3
lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]
solution(lines)

