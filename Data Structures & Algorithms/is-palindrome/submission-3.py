class Solution:
    def isPalindrome(self, s: str) -> bool:
        endPointer = len(s) - 1
        i = 0
        while i < endPointer:
            if not s[endPointer].isalnum():
                endPointer -= 1
                continue
            if not s[i].isalnum():
                i += 1
                continue
            if s[i].lower() == s[endPointer].lower():
                endPointer -= 1
                i += 1
            else:
                return False

        return True