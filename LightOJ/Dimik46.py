import math
def calculateArea(nums):
    s = (nums[0]+nums[1]+nums[2])/2
    return math.sqrt(s*(s-nums[0])*(s-nums[1])*(s-nums[2]))
testCase = int(input())
for case in range(testCase):
    temp = [int(x) for x in input().split()]
    print(f"Area = {calculateArea(temp):.3f}")
