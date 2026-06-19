class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashMap = {}
        for i, num in enumerate(nums):
            if num in hashMap:
                return True
            hashMap[num] = i
        return False
        