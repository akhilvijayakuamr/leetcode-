class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def wrapper(string):
            res = []
            for i in string:
                if i == "#":
                    if res:
                        res.pop()
                else:
                    res.append(i)
            return res
        return wrapper(s) == wrapper(t)

        
        