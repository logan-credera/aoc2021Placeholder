data = open("input.txt").readlines()
# copy the data to a list
tempLst = [d.strip() for d in data]

def splitLines(line):
    coords = line.split(' -> ')
    left = list(map(int, coords[0].split(',')))
    right = list(map(int, coords[1].split(',')))

    return {"left": left, "right": right}

lst = list(map(splitLines, tempLst))

# Above is preprocessing

def createPoints(line):
    points = []
    isX = False

    if (line["left"][1] - line["right"][1] != 0) and (line["left"][0] - line["right"][0]) / (line["left"][1] - line["right"][1]) in [1, -1]: # slope == 1 or -1 is 45
        currXNum = line["left"][0]
        currYNum = line["left"][1]
        while currXNum != line["right"][0]:
            points.append(tuple([currXNum, currYNum]))
            if currXNum < line["right"][0]:
                currXNum += 1
            else:
                currXNum -= 1
            if currYNum < line["right"][1]:
                currYNum += 1
            else:
                currYNum -= 1
        points.append(tuple([currXNum, currYNum]))

        return points
    elif line["left"][0] == line["right"][0] and line["left"][1] == line["right"][1]:
        return [tuple(line["left"])]
    elif line["left"][0] == line["right"][0]:
        pair = [line["left"][1], line["right"][1]]
        staticOne = line["left"][0]
    elif line["left"][1] == line["right"][1]:
        pair = [line["left"][0], line["right"][0]]
        staticOne = line["left"][1]
        isX = True
    else:
        return []

    pair.sort() # sort so range command works
    for num in range(pair[0], pair[1] + 1):# probably a better way to do this
        if isX:
            points.append(tuple([num, staticOne]))
        else:
            points.append(tuple([staticOne, num]))

    return points

allPoints = []
for line in lst:
    allPoints += createPoints(line)

countOverlap = 0
pointsMap = {}

for item in allPoints:
    if not item in pointsMap.keys():
        pointsMap[item] = "present"
    elif pointsMap[item] == "present":
        countOverlap += 1
        pointsMap[item] = "counted"
    else:
        pass

print(countOverlap)
# print(pointsMap)
# print(len(pointsMap.keys()))
# print()
