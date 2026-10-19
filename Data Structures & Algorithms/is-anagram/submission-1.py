class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        
        lst = [0] * 26

        for char in s:
            lst[ord(char) - ord('a')] += 1

        for char in t:
            if lst[ord(char) - ord('a')] == 0:
                return False
            else:
                lst[ord(char) - ord('a')] -= 1

        return True