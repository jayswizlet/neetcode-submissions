class Solution:
    def isPalindrome(self, s: str) -> bool:
        endPointer = len(s)
        frontPointer = 0
        while frontPointer < endPointer:
            if not s[frontPointer].isalnum():
                frontPointer += 1
                continue
            if not s[endPointer-1].isalnum():
                endPointer -= 1
                continue
            if s[frontPointer].lower() == s[endPointer-1].lower():
                endPointer -= 1
                frontPointer += 1
            else:
                return False
        return True
