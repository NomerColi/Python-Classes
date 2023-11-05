patternSelectionRange = ['A', 'B', 'C', 'D']
space = ' '
patternNum = 5
returnMessage = 'Returned to main menu'

#print string with space
def SpacePrint(s, j = 0):
    s = s.replace('ñ', str(j + 1))
    print(s, end= ' ')

def GetSymbol(s, j):
    return s.replace('ñ', str(j + 1))

#symbol input
inputMsgSymbol = "Please enter a symbol. If you want to use numbers, enter 'numbers': "
errMsgSymbol = "Wrong input. Please select a valid input."

def GetSymbolInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if len(s) == 1:
            return s
        elif s == "numbers":
            return 'ñ'
        else:
            print(errMsg)

#pattern selection
inputMsgPatternSelect = '''
A- To print a rectangle
B- To print a Pyramid Pattern
C- To print a Diamond Pattern


Q- To quit.

'''
errMsgPatternSelection = "Wrong input"
def GetPatternSelectionInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if s in patternSelectionRange:
            return s
        else:
            print(errMsg)

#shape input
def GetShapeSelectionInput(shapeNum, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if s.isdigit() and 0 <= int(s) <= shapeNum:
            return int(s)
        else:
            print(errMsg)

#rectangle
#rectangle dimension input
rectDimensionLimit = 10
inputMsgRectDimension = "Enter dimensions of rectangle. (x, y): "
errMsgRectDimension = "Wrong input"

def GetRectDimensionInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        s.replace(' ', '')
        #determine if input is in correct form
        commaIndex = s.find(',')
        if commaIndex != -1 and 0 < commaIndex < len(s) - 1:
            left = s[0:commaIndex]
            right = s[commaIndex + 1:]
            if left.isnumeric() and right.isnumeric():
                xDim = int(left)
                yDim = int(right)
                if xDim < rectDimensionLimit and yDim < rectDimensionLimit:
                    return [xDim, yDim]
        print(errMsg)

#rectangle shape input
rectShapeNum = 2
inputMsgRectShape = '''
1- Hollow Rectangle
2- Solid Rectangle
0- Return to main menu
'''

errMsgRectShape = "Wrong Input"

#rectangle draw functions
def DrawHollowRectangle(dim, symbol):
    print(f"\n Your hollow rectangle with dimensions: ({dim[0]}, {dim[1]}) and symbol '{symbol}'")

    for i in range(dim[1]):
        for j in range(dim[0]):
            if i == 0 or i == dim[1] - 1 or j == 0 or j == dim[0] - 1:
                print(GetSymbol(symbol, j), ' ')
            else:
                print(' ', end=' ')
        print()

def DrawSolidRectangle(dim, symbol):
    print(f"\n Your solid rectangle with dimensions: ({dim[0]}, {dim[1]}) and symbol '{symbol}'")

    for i in range(dim[1]):
        for j in range(dim[0]):
            print(GetSymbol(symbol, j), ' ')
        print()

##Pyramid
#Pyramid Height Input
pyramidHeightLimit = 10
inputMsgHeight = "Enter height: "
errMsgHeight = "Wrong height input"

def GetHeightInput(limit, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        #check if input is integer
        if s.isnumeric() and int(s) < limit:
            return int(s)
        else:
            print(errMsg)

# Pyramid Shape Input
pyramidShapeNum = 2
inputMsgPyramidShape = '''
1- Half Pyramid
2- Full Pyramid
0- Return to main menu
'''
errMsgPyramidShape = "Wrong input"

# Half Pyramid Shape Input
halfPyramidShapeNum = 3
inputMsgHalfPyramidShape = '''
1- Half Pyramid
2- Inverted Half Pyramid
3- Hollow Inverted Half Pyramid
0- Return to main menu
'''
errMsgHalfPyramidShape = "Wrong input"

# Half Pyramid Draw Functions
def DrawHalfPyramid(height, symbol):
    print(f"\nYour half pyramid with height: {height} and symbol '{symbol}'")

    for i in range(height):
        for j in range(0, i + 1):
            print(GetSymbol(symbol, j), end='') 
        print()

def DrawInvertedHalfPyramid(height, symbol):
    print(f"\nYour inverted half pyramid with height: {height} and symbol '{symbol}'")

    for i in range(height, 0, -1):
        for j in range(0, i):
            print(GetSymbol(symbol, j), end='') 
        print()

def DrawHollowInvertedHalfPyramid(height, symbol):
    print(f"\nYour hollow inverted half pyramid with height: {height} and symbol '{symbol}'")

    #SpacedPrint((symbol + space) * height, 0)
    print()
    for i in range(height):
        for j in range(height):
            if i == 0 or j == 0 or i+j == (height-1):
                print(GetSymbol(symbol, j), end='') 
            else:
                print(' ', end='')
        print()

# Full Pyramid Shape Input
fullPyramidShapeNum = 3
inputMsgFullPyramidShape = '''
1- Full Pyramid
2- Inverted Full Pyramid
3- Hollow Inverted Full Pyramid
0- Return to main menu
'''
errMsgFullPyramidShape = "Wrong input"

def DrawFullPyramid(height, symbol):
    print(f"\nYour full pyramid with height: {height} and symbol '{symbol}'")

    h = 0
    for i in range(1, height + 1):
        for j in range(1, (height-i)+1):
            print(end=' ')
        while h != (2*i-1):
            print(GetSymbol(symbol, j), end='') 
            h += 1
        h = 0
        print()

def DrawInvertedFullPyramid(height, symbol):
    print(f"\nYour inverted full pyramid with height: {height} and symbol '{symbol}'")
    for i in range(height, 0, -1):
        for j in range(0, height - i):
            print(end= ' ')
        for j in range(0, i):
            print(GetSymbol(symbol, j), end=' ') 
        print()

def DrawHollowInvertedFullPyramid(height, symbol):
    print(f"\nYour hollow inverted full pyramid with height: {height} and symbol '{symbol}'")
    for i in range(1, height + 1):
        for j in range(1, 2*height):
            if i == 1 or i == j or i + j == 2*height:
                print(GetSymbol(symbol, j), end='') 
            else:
                print(' ', end='')
        print()

##Diamond
#Diamond Height Input
diamondHeightLimit = 10
inputMsgDiamondHeight = "Enter diamond height: "
errMsgHeight = "Wrong height input"

def GetDiamondHeightInput(limit, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if s.isnumeric() and int(s) < limit:
            return int(s)
        else:
            print(errMsg)

#Diamond Shape Input
diamondShapeNum = 3
inputMsgDiamondShape = '''
1- Solid Diamond
2- Hollow Diamond
3- Solid Half Diamond
0- Return to main menu
'''
errMsgDiamondShape = "Wrong input"

def drawSolidDiamond(height, symbol):
    print(f"\nYour solid diamond with height: {height} and symbol '{symbol}'")
    for i in range(height):
        print(' '*(height - i), GetSymbol(symbol, i)*(i*2+1))
    for i in range(height - 2, -1, -1):
        print(' '*(height - i), GetSymbol(symbol, i)*(i*2+1))

def drawHollowDiamond(height, symbol):
    print(f"\nYour hollow diamond with height: {height} and symbol '{symbol}'")
    for i in range(height + 1):
        for j in range(height - i + 1):
            print(" ", end= '')
        for j in range(2 * i):
            if j == 1 or j == 2*i-1:
                print(GetSymbol(symbol, j), end="")
            else:
                print(space, end="")
        print()
    for i in range(height - 1, 0, -1):
        for j in range(height - i + 1):
            print(" ", end= '')
        for j in range(2 * i):
            if j == 1 or j == 2*i-1:
                print(GetSymbol(symbol, j), end="")
            else:
                print(space, end="")
        print()

def drawSolidHalfDiamond(height, symbol):
    print(f"\nYour solid half diamond with height: {height} and symbol '{symbol}'")
    for i in range(height):
        for j in range(i + 1):
            print(GetSymbol(symbol, j), end='')
        print()
    for i in range(1, height):
        for j in range(i, height):
            print(GetSymbol(symbol, j), end="")
        print()

##Put it all together
while True:
    patternSelection = GetPatternSelectionInput(inputMsgPatternSelect, errMsgRectDimension)
    #Rectangle
    if patternSelection == 'A' or patternSelection == 'a':
        dimensions = GetRectDimensionInput(inputMsgRectDimension, errMsgRectDimension)
        symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
        shape = GetShapeSelectionInput(rectShapeNum, inputMsgRectShape, errMsgRectShape)

        if shape == 0:
            print(returnMessage)
            continue
        if shape == 1:
            DrawHollowRectangle(dimensions, symbol)
        elif shape == 2:
            DrawSolidRectangle(dimensions, symbol)

    #Pyramid
    elif patternSelection == 'B' or patternSelection == 'b':
        height = GetHeightInput(pyramidHeightLimit, inputMsgHeight, errMsgHeight)
        symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
        shape = GetShapeSelectionInput(pyramidShapeNum, inputMsgPyramidShape, errMsgPyramidShape)

        if shape == 0:
            print(returnMessage)
            continue
        if shape == 1:
            halfShape = GetShapeSelectionInput(halfPyramidShapeNum, inputMsgHalfPyramidShape, errMsgHalfPyramidShape)

            if halfShape == 0:
                print(returnMessage)
                continue
            elif halfShape == 1:
                DrawHalfPyramid(height, symbol)
            elif halfShape == 2:
                DrawInvertedHalfPyramid(height, symbol)
            elif halfShape == 3:
                DrawHollowInvertedHalfPyramid(height, symbol)

        elif shape == 2:
            fullShape = GetShapeSelectionInput(fullPyramidShapeNum, inputMsgFullPyramidShape, errMsgFullPyramidShape)

            if fullShape == 0:
                print(returnMessage)
                continue
            elif fullShape == 1:
                DrawFullPyramid(height, symbol)
            elif fullShape == 2:
                DrawInvertedFullPyramid(height, symbol)
            elif fullShape == 3:
                DrawHollowInvertedFullPyramid(height, symbol)
    elif patternSelection == 'C' or patternSelection == 'c':
        height = GetHeightInput(diamondHeightLimit, inputMsgHeight, errMsgHeight)
        symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
        shape = GetShapeSelectionInput(diamondShapeNum, inputMsgDiamondShape, errMsgDiamondShape)

        if shape == 0:
            print(returnMessage)
            continue
        if shape == 1:
            drawSolidDiamond(height, symbol)
        elif shape == 2:
            drawHollowDiamond(height, symbol)
        elif shape == 3:
            drawSolidHalfDiamond(height, symbol)

print("Thank you for your business")

