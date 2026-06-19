class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        returnArray = []
        for i in range(len(nums)-2):
            if i > 0 and sortedNums[i] == sortedNums[i-1]:
                continue
            back = len(nums) - 1
            front = i+1
            while front < back:
                total = sortedNums[i] + sortedNums[front] + sortedNums[back]
                if total < 0:
                    front += 1
                    while front < back and sortedNums[front-1] == sortedNums[front]:
                        front += 1
                elif total > 0:
                    back -= 1
                    while front < back and sortedNums[back] == sortedNums[back+1]:
                        back -= 1
                else:
                    returnArray.append([sortedNums[i], sortedNums[front], sortedNums[back]])
                    front += 1
                    while front < back and sortedNums[front-1] == sortedNums[front]:
                        front += 1
                    back -= 1
                    while front < back and sortedNums[back] == sortedNums[back+1]:
                        back -= 1
        return returnArray