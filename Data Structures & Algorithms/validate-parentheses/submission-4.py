class Solution:
    def isValid(self, s: str) -> bool:
        pStack = []
        pDict = {"[" : "]",
                "{" : "}",
                "(" : ")"}

        for p in s:
            if p in pDict:
                pStack.append(p)
            else:
                if pStack and p == pDict.get(pStack[-1]):
                    pStack.pop()
                else:
                    return False
                
        if len(pStack) == 0:
            return True

        return False
            
