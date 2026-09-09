class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        freq_s = {}
        freq_t = {}

        for item in s:
            freq_s[item] = freq_s.get(item,0) + 1

        for item in t:
            freq_t[item] = freq_t.get(item,0) + 1       

        for i in s:
            if freq_s[i] != freq_t.get(i, 0):
                return False

            
        return True