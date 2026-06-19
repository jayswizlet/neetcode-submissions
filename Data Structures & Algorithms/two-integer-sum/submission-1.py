class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i, num in enumerate(nums):
            search = target - num
            if search in hashMap:
                return[hashMap[search], i]
            hashMap[num] = i
