class Solution:
        def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
                #If temp is less than current temp at the top of the stack (pushes from least to greatest)
                #We append the index the stack
                #Thus, we have a stack full of indexes, which is monotonically increasing
                #When we hit a temp that is greater than, what we need to do is ?

                tempStack = []
                results = [0] * len(temperatures)
                for index, temp in enumerate(temperatures):
                        if not tempStack:
                                tempStack.append(index)
                        if temp <= temperatures[tempStack[-1]]:
                                tempStack.append(index)
                        else:
                                while tempStack and temp > temperatures[tempStack[-1]]:
                                        idx = tempStack.pop()
                                        results[idx] = index - idx
                                tempStack.append(index)
                return results
                        
                                