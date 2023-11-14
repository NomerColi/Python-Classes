patternSelectionRange = ['a', 'b', 'c', 'q']
returnMessage = 'Returned to main menu'

#return a string replaced with numbers that come from index 'j'
# s is a symbol that the user entered
# j is an index for printing numbers as a symbol
def GetSymbol(s, j):
    return s.replace('ñ', str(j + 1))

#symbol input
inputMsgSymbol = "Please enter a symbol. If you want to use numbers, enter 'numbers': "
errMsgSymbol = "Wrong input. Please select a valid input."

#get and return a symbol that is either one length or 'numbers'
def GetSymbolInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        if len(s) == 1:
            return s
        elif s == "numbers":
            #'ñ' is a symbol for using numbers, user cannot enter this symbol using a keyboard
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
#get and return a char that is in range of 'patternSelectionRange'
def GetPatternSelectionInput(inputMsg, errMsg):
    while True:
        s = input(inputMsg).lower()
        if s in patternSelectionRange:
            return s
        else:
            print(errMsg)

#shape input
#get and return an integer that is digit between 0 and 'shapeNum'
#shapeNum is a number of shapes that the selected pattern has
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
#get an 
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

#draw hollow rectangle with given dim and given symbol
#dim is a list consisted of x and y value
def DrawHollowRectangle(dim, symbol):
    print(f"\n Your hollow rectangle with dimensions: ({dim[0]}, {dim[1]}) and symbol '{symbol}'")

    for i in range(dim[1]):
        for j in range(dim[0]):
            if i == 0 or i == dim[1] - 1 or j == 0 or j == dim[0] - 1:
                print(GetSymbol(symbol, j), end=' ')
            else:
                print(' ', end=' ')
        print()

#draw solid rectangle with given dim and given symbol
#dim is a list consisted of x and y value
def DrawSolidRectangle(dim, symbol):
    print(f"\n Your solid rectangle with dimensions: ({dim[0]}, {dim[1]}) and symbol '{symbol}'")

    for i in range(dim[1]):
        for j in range(dim[0]):
            print(GetSymbol(symbol, j), end=' ')
        print()

#Rectangle draw process
#get height, symbol, and shape input and draw a rectangle
#return an integer for deciding whether the user wants to quit or not
def RectangleProcess():
    dimensions = GetRectDimensionInput(inputMsgRectDimension, errMsgRectDimension)
    symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
    shape = GetShapeSelectionInput(rectShapeNum, inputMsgRectShape, errMsgRectShape)

    if shape == 0:
        print(returnMessage)
        return -1
    elif shape == 1:
        DrawHollowRectangle(dimensions, symbol)
    elif shape == 2:
        DrawSolidRectangle(dimensions, symbol)

    return 0

##Pyramid
#Pyramid Height Input
pyramidHeightLimit = 10
inputMsgHeight = "Enter height: "
errMsgHeight = "Wrong height input"

#return an integer for height that is less than given limit
def GetHeightInput(limit, inputMsg, errMsg):
    while True:
        s = input(inputMsg)
        #check if input is integer
        if s.isnumeric() and 0 < int(s) < limit:
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

#draw half pyramid with given height and given symbol
def DrawHalfPyramid(height, symbol):
    print(f"\nYour half pyramid with height: {height} and symbol '{symbol}'")

    for i in range(height):
        for j in range(0, i + 1):
            print(GetSymbol(symbol, j), end='') 
        print()

#draw inverted half pyramid with given height and given symbol
def DrawInvertedHalfPyramid(height, symbol):
    print(f"\nYour inverted half pyramid with height: {height} and symbol '{symbol}'")

    for i in range(height, 0, -1):
        for j in range(0, i):
            print(GetSymbol(symbol, j), end='') 
        print()

#draw hollow inverted half pyramid with given height and given symbol
def DrawHollowInvertedHalfPyramid(height, symbol):
    print(f"\nYour hollow inverted half pyramid with height: {height} and symbol '{symbol}'")

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

#draw full pyramid with given height and given symbol
def DrawFullPyramid(height, symbol):
    print(f"\nYour full pyramid with height: {height} and symbol '{symbol}'")

    h = 0
    for i in range(1, height + 1):
        for j in range(1, (height-i)+1):
            print(end=' ')
        while h != (2*i-1):
            print(GetSymbol(symbol, h if (h < i) else i*2 - h - 2), end='')
            h += 1
        h = 0
        print()

#draw inverted full pyramid with given height and given symbol
def DrawInvertedFullPyramid(height, symbol):
    print(f"\nYour inverted full pyramid with height: {height} and symbol '{symbol}'")
    for i in range(height, 0, -1):
        for j in range(0, height - i):
            print(end= ' ')
        for j in range(0, i*2 - 1):
            print(GetSymbol(symbol, j if (j < i) else i*2 - j - 2), end='')
        print()

#draw hollow inverted full pyramid with given height and given symbol
def DrawHollowInvertedFullPyramid(height, symbol):
    print(f"\nYour hollow inverted full pyramid with height: {height} and symbol '{symbol}'")
    for i in range(1, height + 1):
        for j in range(1, 2*height):
            if i == 1 or i == j or i + j == 2*height:
                idx = 0
                if i == 1:
                    idx = j - 1 if (j <= height) else height*2 - j - 1
                print(GetSymbol(symbol, idx), end='')
            else:
                print(' ', end='')
        print()

#Pyramid Process
#get height, symbol, and shape input and draw a pyramid
#return an integer for deciding whether the user wants to quit or not
def PyramidProcess():
    height = GetHeightInput(pyramidHeightLimit, inputMsgHeight, errMsgHeight)
    symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
    shape = GetShapeSelectionInput(pyramidShapeNum, inputMsgPyramidShape, errMsgPyramidShape)

    if shape == 0:
        print(returnMessage)
        return -1
    if shape == 1:
        #let user choose which half pyramid pattern to print
        halfShape = GetShapeSelectionInput(halfPyramidShapeNum, inputMsgHalfPyramidShape, errMsgHalfPyramidShape)

        if halfShape == 0:
            print(returnMessage)
            return -1
        elif halfShape == 1:
            DrawHalfPyramid(height, symbol)
        elif halfShape == 2:
            DrawInvertedHalfPyramid(height, symbol)
        elif halfShape == 3:
            DrawHollowInvertedHalfPyramid(height, symbol)

    elif shape == 2:
        #let user choose which full pyramid pattern to print
        fullShape = GetShapeSelectionInput(fullPyramidShapeNum, inputMsgFullPyramidShape, errMsgFullPyramidShape)

        if fullShape == 0:
            print(returnMessage)
            return -1
        elif fullShape == 1:
            DrawFullPyramid(height, symbol)
        elif fullShape == 2:
            DrawInvertedFullPyramid(height, symbol)
        elif fullShape == 3:
            DrawHollowInvertedFullPyramid(height, symbol)
    return 0

##Diamond
#Diamond Height Input
diamondHeightLimit = 10
inputMsgDiamondHeight = "Enter diamond height(less than 10): "
errMsgHeight = "Wrong height input"

#Diamond Shape Input
diamondShapeNum = 3
inputMsgDiamondShape = '''
1- Solid Diamond
2- Hollow Diamond
3- Solid Half Diamond
0- Return to main menu
'''
errMsgDiamondShape = "Wrong input"

#draw solid diamond with given height and given symbol
def DrawSolidDiamond(height, symbol):
    print(f"\nYour solid diamond with height: {height} and symbol '{symbol}'")
    for i in range(height):
        print(' '*(height - i), GetSymbol(symbol, i)*(i*2+1))
    for i in range(height - 2, -1, -1):
        print(' '*(height - i), GetSymbol(symbol, i)*(i*2+1))

#draw solid hollow diamond with given height and given symbol
def DrawHollowDiamond(height, symbol):
    print(f"\nYour hollow diamond with height: {height} and symbol '{symbol}'")
    for i in range(height + 1):
        for j in range(height - i + 1):
            print(" ", end= '')
        for j in range(2 * i):
            if j == 1 or j == 2*i-1:
                print(GetSymbol(symbol, j), end="")
            else:
                print(' ', end="")
        print()
    for i in range(height - 1, 0, -1):
        for j in range(height - i + 1):
            print(" ", end= '')
        for j in range(2 * i):
            if j == 1 or j == 2*i-1:
                print(GetSymbol(symbol, j), end="")
            else:
                print(' ', end="")
        print()

#draw solid half diamond with given height and given symbol
def DrawSolidHalfDiamond(height, symbol):
    print(f"\nYour solid half diamond with height: {height} and symbol '{symbol}'")
    for i in range(height):
        for j in range(i + 1):
            print(GetSymbol(symbol, j), end='')
        print()
    for i in range(1, height):
        for j in range(i, height):
            print(GetSymbol(symbol, j), end="")
        print()

#Diamond Process
#get height, symbol, and shape input and draw a diamond
#return an integer for deciding whether the user wants to quit or not
def DiamondProcess():
    height = GetHeightInput(diamondHeightLimit, inputMsgHeight, errMsgHeight)
    symbol = GetSymbolInput(inputMsgSymbol, errMsgSymbol)
    shape = GetShapeSelectionInput(diamondShapeNum, inputMsgDiamondShape, errMsgDiamondShape)

    if shape == 0:
        print(returnMessage)
        return -1
    if shape == 1:
        DrawSolidDiamond(height, symbol)
    elif shape == 2:
        DrawHollowDiamond(height, symbol)
    elif shape == 3:
        DrawSolidHalfDiamond(height, symbol)
    
    return 0

#main process
#get an input for choosing which pattern to print and process
#return an integer for deciding whether the user wants to quit or not
def Process():
    patternSelection = GetPatternSelectionInput(inputMsgPatternSelect, errMsgRectDimension)

    if patternSelection == 'a':
        return RectangleProcess()
    elif patternSelection == 'b':
        return PyramidProcess()
    elif patternSelection == 'c':
        return DiamondProcess()
    elif patternSelection == 'q':
        return -1

#main code
while True:
    #process the painting and saves the result value
    result = Process()
    #result is -1 when the user inputs 'q' to quit
    if result == -1:
        break

print("Thank you for your business")

