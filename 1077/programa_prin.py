import math
while True:
    try: 
        def romano(A):
            romansDict = \
                {
                    1: "i",
                    5: "v",
                    10: "x",
                    50: "l",
                    100: "c",
                    500: "d",
                    1000: "m",
                    5000: "g",
                    10000: "h"
                }
  
            div = 1
            while A >= div:
                div *= 10
            div /= 10
            res = ""
            while A:
                lastNum = int(A / div)
                if lastNum <= 3:
                    res += (romansDict[div] * lastNum)
                elif lastNum == 4:
                    res += (romansDict[div] +
                                romansDict[div * 5])
                elif 5 <= lastNum <= 8:
                    res += (romansDict[div * 5] +
                    (romansDict[div] * (lastNum - 5)))
                elif lastNum == 9:
                    res += (romansDict[div] +
                                romansDict[div * 10])
                A = math.floor(A % div)
                div /= 10
            return res
        n=int(input())
        if(n==0):
            break
        else:
            z=str(romano(n))
            print(n,"=>",z)
    except EOFError:
        break