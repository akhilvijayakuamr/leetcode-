class Solution:
    def removeStars(self, s: str) -> str:
        res = []
        for i in range(len(s)):
            if s[i]!='*':
                res.append(s[i])
            else:
                res.pop()
        return "".join(res)