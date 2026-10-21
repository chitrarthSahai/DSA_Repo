class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Approach using dictionary with char count array as key and list of words

        ansDict = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for char in word:
                idx = ord(char) - ord('a')
                count[idx] += 1
            
            ansDict[tuple(count)].append(word)
        
        #Is generator expression faster than list comprehension?
        return list(ansDict.values())