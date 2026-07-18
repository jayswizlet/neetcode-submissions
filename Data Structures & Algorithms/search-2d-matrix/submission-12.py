class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Binary search on rows -> Binary search on columns
        #If binary search on columns fail then we return false'
        if not matrix or not matrix[0]:
            return False

        mLow = 0
        mHigh = len(matrix)-1
        mMid = (mHigh + mLow) // 2

        while mLow <= mHigh:
            mMid = (mHigh + mLow) // 2
            if matrix[mMid][0] == target:
                return True
            if target < matrix[mMid][0]:
                mHigh = mMid - 1
            else:
                mLow = mMid + 1

        nLow = 0
        nHigh = len(matrix[0])-1

        row = mHigh
        if row < 0:
            return False
        
        while nLow <= nHigh:
            nMid = (nHigh + nLow) // 2
            if matrix[row][nMid] == target:
                return True
            if target <  matrix[row][nMid]:
                nHigh = nMid - 1
            else:
                nLow = nMid + 1

        return False
