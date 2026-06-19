class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashMap = {}
        # freq = [[] for i in range len(nums+1)]
        dupeList = []
        for num in nums:
            if num in hashMap:
                hashMap[num] += 1
            else:
                hashMap[num] = 1
        
        for num, count in hashMap.items():
            dupeList.append([count, num])
        dupeList.sort()

        res = []
        while len(res) < k:
            res.append(dupeList.pop()[1])
        return res
        
        