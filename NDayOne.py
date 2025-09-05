class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in nums:
            count = 0
            for x in range(0, len(nums)):
                if nums[x] == i:
                    count+=1
                    if count == 2: return True

        return False

# contains duplicate