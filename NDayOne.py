# Initial solution, O(N^2) complexity
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            count = 0
            for x in range(0, len(nums)):
                if nums[x] == i:
                    count+=1
                    if count == 2: return True

        return False

# Final solution, O(N) complexity
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        uniqueNums = list(set(nums))
        if len(uniqueNums) == len(nums):
            return False
        else: 
            return True
        
#problem name: contains duplicate
