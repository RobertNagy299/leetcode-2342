# 2342. max sum of pair with equal sum of digits - medium
# Solved without any help, beats 38%. Rt: 426ms

from typing import List
from collections import defaultdict
class Solution:
    
    
    def maximumSum(self, nums: List[int]) -> int:
        # n = len(nums)
        
        # myHashMap looks like this:
        # key : sum -> value : (freq, biggestNum1, biggestNum2)
        myHashMap = defaultdict(tuple)
        
        # Auxiliary function to determine the second largest number in a tuple of 3 integers
        def secondMax(num1: int, num2: int, num3: int) -> int:
            return min(max(num1, num2), num3 )
        
        # Auxiliary function to calculate the sum of an integer's digits
        def sumOfDigits(number: int) -> int:
            sum = 0
            while number > 0:
                sum += number % 10
                number = number // 10
            return sum
        
        ans = -1
        
        for num in nums:
            digitsum = sumOfDigits(num)
           # print(f"Digit sum = {digitsum} for num = {num}")
            initialTuple = myHashMap.get(digitsum, (0, 0,0)) 

            # We map a tuple to each sum value.
            # For each "digit sum" I maintain a tuple that contains its frequency 
            # frequency, in this context, means the number of integers that have the same digit sum
            # and I also store the two biggest numbers that have the same "digit sum"
            myHashMap[digitsum] = (initialTuple[0] + 1, max(initialTuple[1], num, initialTuple[2]), secondMax(initialTuple[1] ,initialTuple[2], num))
            
            # If there are at least 2 numbers with the same "digit sum"
            # And if their sum is greater than the current biggest sum
            # Update the answer
            sumOfPairs = myHashMap[digitsum][1] + myHashMap[digitsum][2]
            if myHashMap[digitsum][0] > 1 and sumOfPairs > ans:
                ans = sumOfPairs
      
        return ans
        # Worst case: O(9*n) because at most, each number will be 9 digits long (based on the constraints)
    

s = Solution()
nums = [368,369,307,304,384,138,90,279,35,396,114,328,251,364,300,191,438,467,183]
print(f"max = {s.maximumSum(nums=nums)}")  