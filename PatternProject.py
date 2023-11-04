patternSelectionRange = ['A', 'B', 'C', 'Q']
space = ' '
patternNum = 5
msgReturnToMenu = "Returned to main menu"

# Printing string with space
def SpacedPrint(s, j):
    s = s.replace('ñ', str(j + 1))
    print(s, end=' ')

# Symbol Input
inputMsgSymbol = "Enter a symbol, if you want to use numbers, enter 'numbers': "
errMsgSymbol = "Wrong input"
def GetSymbolInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if len(s) == 1:
            return s
        elif s == "numbers":
            return 'ñ'
        else:
            print(errMsg)

# Pattern Selection
inputMsgPatternSelection = '''
A- To print a rectangle
B- To print Pyramid pattern
C- To print Diamond Pattern

Q- To quit.
'''
errMsgPatternSelection = "Wrong input"
def GetPatternSelectionInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        # check if the input value is one of the options
        if s in patternSelectionRange:
            return s
        else:
            print(errMsg)

# Shape Input
def GetShapeSelectionInput(shapeNum, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if s.isdigit() and 0 <= int(s) <= shapeNum:
            return int(s)
        else:
            print(errMsg)

## Rectangle
# Rectangle Dimension Input
rectDimensionLimit = 10
inputMsgRectDimension = "Enter dimensions of rectangle. (x, y): "
errMsgRectDimension = "Wrong input"
def GetRectDimensionInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        s.replace(' ', '')
        # check if the input value is in right form
        commaIndex = s.find(',')
        if commaIndex != -1 and 0 < commaIndex < len(s) - 1:
            left = s[0:commaIndex]
            right = s[commaIndex + 1:]
            if left.isnumeric() and left.isnumeric():
                xDim = int(left)
                yDim = int(right)
                if xDim < rectDimensionLimit and yDim < rectDimensionLimit:
                    return [xDim, yDim]

        print(errMsg)

# Rectangle Shape Input
rectShapeNum = 2
inputMsgRectShape = '''
1- Hollow Rectangle
2- Solid Rectangle
0- Return to main menu
'''
errMsgRectShape = "Wrong input"

# Rectangle Draw Functions
def DrawHollowRectangle(dim, symbol):
    print(f"\nYour hollow rectangle with dimensions: ({dim[0]}, {dim[1]}) and symbol '{symbol}'")

    for i in range(dim[1]):
        for j in range(dim[0]):
            if i == 0 or i == dim[1] - 1 or j == 0 or j == dim[0] - 1:
                SpacedPrint(symbol)
            else:
                SpacedPrint(space)
        print()

def DrawSolidRectangle(dim, symbol):
    print(f"\nYour rectangle with dimensions: ({dim[0]}, {dim[1]}) and symbol '{symbol}'")

    for i in range(dim[1]):
        for j in range(dim[0]):
            SpacedPrint(symbol)
        print()

## Pyramid
# Pyramid Height Input
pyramidHeightLimit = 10
inputMsgHeight = "Enter height: "
errMsgHeight = "Wrong height input"
def GetHeightInput(limit, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        # check if the input value is integer
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
        for j in range(height):
            if i >= j:
                SpacedPrint(symbol, j)
        print()

def DrawInvertedHalfPyramid(height, symbol):
    print(f"\nYour inverted half pyramid with height: {height} and symbol '{symbol}'")

    for i in range(height):
        for j in range(height):
            if i <= j:
                SpacedPrint(symbol, j)
        print()

def DrawHollowInvertedHalfPyramid(height, symbol):
    print(f"\nYour hollow inverted half pyramid with height: {height} and symbol '{symbol}'")

    #SpacedPrint((symbol + space) * height, 0)
    print()
    for i in range(height):
        for j in range(height):
            if i == 0 or j == 0 or i == height - 1 - j:
                SpacedPrint(symbol, j)
            else:
                SpacedPrint(space, j)
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

# Full Pyramid Draw Functios
def DrawFullPyramid(height, symbol):
    print()

# def HallowSomething(v, h):
#     print(star * v)
#     for i in range(v):
#         for j in range(i, h):
#             print(space, end=' ')
#         for j in range(i + 1):
#             print(star, end=space)

# def HallowSomething(v, h):
#     print(star * v)
#     for i in range(1, h + 1):
#         for j in range(i, h):
#             print(space, end=' ')
#         for j in range(i + 1):
#             print(star, end=' ')
#         for j in range(v):
#             print(star, end=' ')

while True:
    # Pattern Selectin
    patternSelection = GetPatternSelectionInput(inputMsgPatternSelection, errMsgRectDimension)
    if patternSelection == 'Q':
        print("End")
        break

    symbol = '*'

    # Rectangle
    if patternSelection == 'A':
        dimensions = GetRectDimensionInput(inputMsgRectDimension, errMsgRectDimension)
        symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
        shape = GetShapeSelectionInput(rectShapeNum, inputMsgRectShape, errMsgRectShape)
        
        if shape == 0:
            print(msgReturnToMenu)
            continue
        if shape == 1:
            DrawHollowRectangle(dimensions, symbol)
        elif shape == 2:
            DrawSolidRectangle(dimensions, symbol)

    # Pyramid
    elif patternSelection == 'B':
        height = GetHeightInput(pyramidHeightLimit, inputMsgHeight, errMsgHeight)
        symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
        shape = GetShapeSelectionInput(pyramidShapeNum, inputMsgPyramidShape, errMsgPyramidShape)
        
        if shape == 0:
            print(msgReturnToMenu)
            continue
        if shape == 1:
            halfShape = GetShapeSelectionInput(halfPyramidShapeNum, inputMsgHalfPyramidShape, errMsgHalfPyramidShape)
            
            if halfShape == 0:
                print(msgReturnToMenu)
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
                print(msgReturnToMenu)
                continue
            elif fullShape == 1:
                DrawFullPyramid(height, symbol)
            

print("Thank you for your business")