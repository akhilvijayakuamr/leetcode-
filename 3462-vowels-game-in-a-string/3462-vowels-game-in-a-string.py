class Solution:
    def doesAliceWin(self, s: str) -> bool:
        k = ['a', 'e', 'i', 'o', 'u']
        for i in range(len(s)):
            if s[i] in k:
                return True
        return False