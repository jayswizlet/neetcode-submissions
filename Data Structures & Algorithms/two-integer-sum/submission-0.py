class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, nums in enumerate(nums):
            search = target - nums
            if search in hashMap:
                return [hashMap[search], i]
            hashMap[nums] = i
    


#if mod not in hashmap
#list with itself
