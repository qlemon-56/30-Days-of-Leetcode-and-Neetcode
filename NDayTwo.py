class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        indices = {}
            
        for n, m in enumerate(nums):
            
            indices[m] = n

        for i, j in enumerate(nums):

            if target - j in indices.keys():
                if i != indices[target-j]:
                    return [i , indices[target-j]]
                    
# final solution, O(N) complexity
                
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        for i in enumerate(nums):
            for x in enumerate(nums):
                if i[0] == x[0]:

                    continue

                if i[1]+x[1] == target:
                    
                    return [i[0], x[0]]


# initial solution

# problem name = two_sum
# what i learnt
#.index() array method return the position of the first occurence of the argument
# using enumerate() is better in for loops because it keeps note of the index and the value at that index
# i leart how to use .keys() and .values() methods for hashmaps
