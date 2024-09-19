import copy
import point


def movePoint(pt):
    pt.translate(1, 1)
    print(pt)


def newPoint():
    return point.Point()

def main():

    p1 = point.Point(1, 2)
    p1.translate(2, 3)
    print(p1)

    p2 = copy.deepcopy(p1)
    p2.translate(1, 1)
    print(p1)
    print(p2)


main()