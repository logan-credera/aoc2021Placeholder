data = open("input.txt").readlines()
# copy the data to a list
lst = [d.strip() for d in data]

def inputCom(wxyz, varOne, initialInteger):
    wxyz[varOne] = initialInteger.pop()
    return wxyz

def addCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] + varTwo
    return wxyz

def mulCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] * varTwo
    return wxyz

def divCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] / varTwo
    return wxyz

def modCom(wxyz, varOne, varTwo):
    wxyz[varOne] = wxyz[varOne] % varTwo
    return wxyz

def eqlCom(wxyz, varOne, varTwo):
    if wxyz[varOne] == varTwo:
        wxyz[varOne] = 1
    else:
        wxyz[varOne] = 0
    return wxyz

def parseInstruction(iptLine, wxyz, monadCode):
    comm = iptLine[:3]
    varOne = iptLine[4]

    if len(iptLine) >= 7:
        if iptLine[6] in ['w', 'x', 'y', 'z']:
            varTwo = wxyz[iptLine[6]]
        else:
            varTwo = int(iptLine[6:])

    if comm == "inp":
        wxyz = inputCom(wxyz, varOne, monadCode)
    elif comm == "mul":
        wxyz = mulCom(wxyz, varOne, varTwo)
    elif comm == "add":
        wxyz = addCom(wxyz, varOne, varTwo)
    elif comm == "eql":
        wxyz = eqlCom(wxyz, varOne, varTwo)
    elif comm == "div":
        wxyz = divCom(wxyz, varOne, varTwo)
    elif comm == "mod":
        wxyz = modCom(wxyz, varOne, varTwo)

    return wxyz

def checkMonad(monadCode):
    wxyz = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    for line in lst:
        wxyz = parseInstruction(line, wxyz, monadCode)

    if wxyz["z"] == 0:
        return False
    return True

def incrementIntList(intList):
    curIndex = -1
    dontExit = True
    while dontExit:
        if intList[curIndex] > 1:
            intList[curIndex] = intList[curIndex] - 1
            dontExit = False
        elif intList[curIndex] == 1:
            intList[curIndex] = 9
            curIndex -= 1

    return intList


initialInteger = [9, 9, 9, 9, 9,
                  9, 9, 9, 9, 9,
                  9, 9, 9, 10]

shouldContinue = True
i = 0
while shouldContinue:
    initialInteger = incrementIntList(initialInteger)
    shouldContinue = checkMonad(initialInteger.copy())
    i += 1

    print("run num", i)
    print(initialInteger)

