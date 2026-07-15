class Solution:
    def minWindow(self, s: str, t: str) -> str:
        target = {}
        for ch in t:
            if target.get(ch):
                target[ch] += 1
            else:
                target[ch] = 1
        
        window = {}
        formed = 0
        left = right = 0
        min_length = float('inf')
        indexes = (-1,-1)
        while right < len(s):
            if s[right] in target:
                window[s[right]] = window.get(s[right],0) + 1
                if target[s[right]] == window[s[right]]:
                    formed += 1
            while formed == len(target):
                if right - left + 1 < min_length:
                    min_length = right - left + 1
                    indexes = (left,right)
                if s[left] in window:
                    window[s[left]] -= 1
                if s[left] in target and window[s[left]] < target[s[left]]:
                    formed -= 1
                left += 1
            right += 1
        
        return s[indexes[0]:indexes[1]+ 1]
