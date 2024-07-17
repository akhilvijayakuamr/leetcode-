class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        hash = {}
        for row in grid:
            for val in row:
                if val in hash:
                    hash[val] = hash[val]+1
                else:
                    hash[val] = 1
        n = len(grid)
        i = 1
        rep, mis = 0, 0
        while(i<=n*n):
            if i not in hash:
                mis = i
            else:
                if hash[i] == 2:
                    rep = i
            i+=1
        return [rep,mis]

        