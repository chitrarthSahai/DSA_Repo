class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ansDict = defaultdict(list)
        
        for word in strs:
            key = "".join(sorted(word))
            ansDict[key].append(word)

        return [vals for vals in ansDict.values()]
