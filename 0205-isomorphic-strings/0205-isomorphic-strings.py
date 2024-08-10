class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = dict()
        check = set()

        for i in range(len(s)):

            if s[i] in hash:
                if hash[s[i]] != t[i]:
                    return False
            else:
                if t[i] in check:
                    return False

            hash[s[i]] = t[i]
            check.add(t[i])

        return True
            
        


            
            