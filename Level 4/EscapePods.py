def solution(entrances, exits, path):
    ent = len(entrances)
    pathLen = len(path)
    exitLen = len(exits)
    count = 0
    middlePath = path[ent:(pathLen-exitLen)]
    for i in range(pathLen - ent - exitLen):
        sumRange = sum(middlePath[i])
        sumEnter = 0
        for j in entrances:
            sumEnter += path[j][ent + i]
        count += min(sumEnter, sumRange)
    return count