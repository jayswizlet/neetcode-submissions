class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Max Height * Distance
        #Min (height1, height2) -> 7,6 = 6
        #Size heights is a list, it will take O(N) to even get the length of it
        area = 0
        for i in range(len(heights)-1):
            # if j == 0:
            #     continue
            for j in range(i+1, len(heights)):
                minHeight = min(heights[i], heights[j])
                distance = j-i
                newArea = minHeight * distance
                if newArea > area:
                    area = newArea
        return area




        