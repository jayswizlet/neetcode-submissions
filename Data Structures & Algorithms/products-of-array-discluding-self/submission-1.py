class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #At index i:
            #Product of left of the number and right of the number
            #Iterate through
                #If less than i -> multiply product and place [Left Side]
                #If greater than i -> also multiply product and place
        
        arrOut = [0] * len(nums)
        product = 1
        for i in range(len(nums)):
            for j in range(len(nums)):
                if j != i:
                    product *= nums[j]
            arrOut[i] = product
            product = 1
        return arrOut
