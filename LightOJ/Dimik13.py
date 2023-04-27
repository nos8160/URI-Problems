def doFactorial(num):
    value = 1
    for val in range(num,1,-1):
        value *= val
    return value

def findDivisor(words):
    wordict = {}
    divisor = 1
    for i in words:
        if i not in wordict:
            wordict[i] = 0
        wordict[i] += 1
    for key in wordict.values():
        if key>1:
            divisor *= doFactorial(key)
    if divisor>0:
        return divisor
    else:
        return 1
testCase = int(input())
for case in range(testCase):
    temp = input().strip().split(" ")
    probability = int(doFactorial(len(temp))/findDivisor(temp))
    print(f"1/{probability}")
