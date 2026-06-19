class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groupDict = {}
        result = []
        
        for word in strs:
            key = tuple(sorted(word))
            if key not in groupDict:
                groupDict[key] = []
            groupDict[key].append(word)
        
        return list(groupDict.values())