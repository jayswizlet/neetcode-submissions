class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashMapS = {}
        hashMapT = {}
        for letter in s:
            if letter in hashMapS:
                hashMapS[letter] += 1
            else:
                hashMapS[letter] = 1
        for letter in t:
            if letter in hashMapT:
                hashMapT[letter] += 1
            else:
                hashMapT[letter] = 1
        return hashMapS == hashMapT