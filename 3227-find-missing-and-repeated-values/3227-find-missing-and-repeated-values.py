class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        val = []
        rep = 0
        mis = 0
        for i in grid:
            val.extend(i)
        val.sort()
        x = 1
        for i in range(len(val)-1):
            if val.count(x) == 0:
                mis = x
            x+=1
            if val.count(val[i]) == 2:
                rep = val[i]
        if mis == 0:
            mis = val[len(val)-1]+1
        return [rep,mis]

            

        