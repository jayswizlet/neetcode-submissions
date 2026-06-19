class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        #Take the difference, and if i is less than index1, we increment
        index1 = 1
        index2 = len(numbers)
        while index1 < index2:
            sum = numbers[index1-1] + numbers[index2-1]
            if sum < target:
                index1 += 1
            elif sum > target:
                index2 -= 1
            elif sum == target:
                return [index1, index2]