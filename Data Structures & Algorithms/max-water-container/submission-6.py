class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #Max Height * Distance
        #Min (height1, height2) -> 7,6 = 6
        #Size heights is a list, it will take O(N) to even get the length of it

        #Brute Force Solution
        # area = 0
        # for i in range(len(heights)-1):
        #     # if j == 0:
        #     #     continue
        #     for j in range(i+1, len(heights)):
        #         minHeight = min(heights[i], heights[j])
        #         distance = j-i
        #         newArea = minHeight * distance
        #         if newArea > area:
        #             area = newArea
        # return area

        front = 0
        back = len(heights)-1
        area = 0
        while front < back:

            minHeight = min(heights[front], heights[back])
            distance = back - front
            newArea = minHeight * distance
            if newArea > area:
                area = newArea
            
            #Increment Front
            if heights[back] > heights[front]:
                front += 1
            else:
                back -= 1

        return area



        