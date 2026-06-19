class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        curr = 0

        for tok in range(len(tokens)):
            if tokens[tok] == '+':
                a = int(numStack.pop())
                b = int(numStack.pop())
                numStack.append(b+a)
            elif tokens[tok] == '/':
                a = int(numStack.pop())
                b = int(numStack.pop())
                numStack.append(b/a)
            elif tokens[tok] == '*':
                a = int(numStack.pop())
                b = int(numStack.pop())
                numStack.append(b*a)
            elif tokens[tok] == '-':
                a = int(numStack.pop())
                b = int(numStack.pop())
                numStack.append(b-a)
            else:
                numStack.append(tokens[tok])
        return int(numStack.pop())