class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        odd = 0
        for key, val in Counter(s).items(): 
            res += val - odd if val % 2 else val
            odd = 1 if val % 2 else odd
        return res

        