import itertools

# Jeste se na to podivat

def refSolution(n):
    ways = [0]*210
    ways[0] = 1
    for x in [1,2,5,10,20,50,100,200]:
        for i in range(x, 201):
            ways[i] += ways[i-x]
    for x in range(0,n):
        print("x:{} = ways:{}".format(x,ways[x]))
    return ways[n]



#
# aimValue = 200
# attemptValue = aimValue
# correct_permutation = 0
# limit = len(arrayValues)
#
# while limit >= 0:
#     for x in arrayValues[:limit]:
#         while(attemptValue > 0):
#             attemptValue -= x
#             print(attemptValue)
#         if(attemptValue == 0):
#             correct_permutation += 1
#             attemptValue = aimValue
#         if(attemptValue <= 0):
#             attemptValue = aimValue
#
#

arrayValues = [ 200, 100, 50, 20, 10 , 5]
numOfUsing = {5: 0,
              10: 0,
              20: 0,
              50: 0,
              100: 0,}


def howManyWays(sumNumber):
    '''
    Counting how many ways can I get sumNumber withou using 2
    :param sumNumber:
    :return:
    '''
    way = 1
    n = sumNumber
    for x in arrayValues:
        n = sumNumber
        if(x > sumNumber):
            continue
        else:
            while n >= x :
                n -= x
                way += 1

            while n >= arrayValues[-1]:
                for xx in arrayValues:
                    n -= xx
                    way += 1



    return way

def getListOfPossibleRemaining(maxValue):
    list = [maxValue]
    if(maxValue % 2 == 0):
        list.append(0)
    n = maxValue
    while True:
        n -= 2
        if n <= 0:
            break
        list.append(n)
    print(list)
    return list

def solutionOfProblem(maxNumber):
    ways = 0
    # print("For max number {}".format( maxNumber))
    for x in getListOfPossibleRemaining(maxNumber):
        ways += howManyWays(x)
        print("For x:{} is ways: {}".format(x, howManyWays(x)))
    return  ways


# limit = 5
# sumWays = 1
# for x in getListOfPossibleRemaining(limit):
#     sumWays += howManyWays(x)
#
# print(sumWays)

import unittest

class UnitTest(unittest.TestCase):
    knownValue = ( (10,11),
                   (6,5),
                   (11,12),
                   (12,12),
                   (1,1),
                   (2,2),
                   (3,2),
                   (4,3),
                   (7,6),
                   (8,7),
                   (9,8),
                   (5,4))
    def test_known_value(self):
        for x in range(1,20,1):
            resultRef = refSolution(x)
            resultMy = solutionOfProblem(x)
            try:
                self.assertEqual(resultMy, resultRef)
            except AssertionError as e:
                print('For x={}'.format(x))
                raise

if __name__ == "__main__":
    # unittest.main()
    # print(solutionOfProblem(11))
    refSolution(201)
