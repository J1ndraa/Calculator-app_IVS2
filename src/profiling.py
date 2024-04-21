from math_library import MathLib
nums = ([float(num) for num in input().split()])
print(MathLib.sqrt(MathLib.mul(MathLib.div(1, len(nums) - 1), MathLib.sub(sum(MathLib.expo(num, 2) for num in nums), MathLib.mul(len(nums), MathLib.expo(sum(nums) / float(len(nums)), 2)))), 2))