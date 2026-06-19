class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        dupeNums = sorted(nums)
        counter = 0
        setter = 0
        for i in range(len(dupeNums)):
            if i + 1 < (len(dupeNums)):
                if dupeNums[i+1] == dupeNums[i] + 1:
                    counter += 1
                elif dupeNums[i+1] != dupeNums[i] + 1 and dupeNums[i+1] != dupeNums[i]:
                    if counter > setter:
                        setter = counter
                    counter = 0
        if counter > setter:
            setter = counter
        if len(dupeNums) > 0:
            setter += 1
        return setter
