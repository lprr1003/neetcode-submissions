class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) == len(t):

            dicts, dictt = {}, {}
            for i in range(len(s)):
                dicts[s[i]] = dicts.get(s[i], 0) + 1
                dictt[t[i]] = dictt.get(t[i], 0) + 1

            return dicts==dictt
        return False

