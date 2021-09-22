from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> List[int]:
        j = 0
        n = len(nums)
        for num in nums:
            if(num != 0):
                nums[j] = num
                j += 1

        for x in range (j, n):
            nums[x] = 0
        return nums

# Call 
arr = [0,1,0,3,12]
solution = Solution()
print(solution.moveZeroes(arr))

##############################
#Another way with List comprehension:

def moveZeroes(arr):
    return [i for i in arr if i != 0] + [0] * arr.count(0)

fastSolution = moveZeroes(arr)
print(fastSolution)