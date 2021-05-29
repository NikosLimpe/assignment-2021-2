def gcd(a, b):
    if (b == 0):
        return a
    return gcd(b, a % b)


# method returns reduced form of dy/dx as a pair
def getReducedForm(dy, dx):
    g = gcd(abs(dy), abs(dx))

    # get sign of result
    sign = (dy < 0) ^ (dx < 0)

    if (sign):
        return (-abs(dy) // g, abs(dx) // g)
    else:
        return (abs(dy) // g, abs(dx) // g)


def findAllReducedForms(points, N, xO, yO):
    st = dict()

    for i in range(N):

        # get x and y co-ordinate of current point
        curX = points[i][0]
        curY = points[i][1]

        temp = getReducedForm(curY - yO, curX - xO)

        # if this slope is not there in set,
        # increase ans by 1 and insert in set
        if (temp not in st):
            st[temp] = []

    return st


# /* method returns minimum number of lines to
#     cover all points where all lines goes
#     through (xO, yO) */
def minLinesToCoverPoints(points, N, xO, yO):
    # set to store slope as a pair
    st = dict()
    minLines = 0
    li = []
    subLi = []
    gg = findAllReducedForms(points, N, xO, yO)
    # loop over all points once
    for i in range(N):

        # get x and y co-ordinate of current point
        curX = points[i][0]
        curY = points[i][1]

        temp = getReducedForm(curY - yO, curX - xO)

        if (temp in gg):
            cell = [points[i][0], points[i][1]]
            gg[temp].append(cell)
        # if this slope is not there in set,
        # increase ans by 1 and insert in set
        if (temp not in st):
            st[temp] = 1
            minLines += 1

    return gg


if __name__ == '__main__':

    # Driver code
    xO = 1
    yO = 0

    points = [[-1, 3],
              [4, 3],
              [2, 1],
              [-1, -2],
              [3, -3]]
    # points = [[1, 1], [2, 2], [3, 3], [4, 4], [5, 5], [6, 6], [11, 4], [11, 5], [11, 6], [10, 1], [10, 2],
    #           [10, 3], [7, 2], [8, 4], [9, 6], [7, 1], [8, 3], [9, 5]]
    N = len(points)
    print(list(minLinesToCoverPoints(points, N, xO, yO).values()))
    cover_points = list(minLinesToCoverPoints(points, N, xO, yO).values())
    print(cover_points)
    for i in cover_points:
        print(str(i) + "\n")
