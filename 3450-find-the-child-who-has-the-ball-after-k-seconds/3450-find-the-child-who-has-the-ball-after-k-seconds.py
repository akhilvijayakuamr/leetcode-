class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        flag = True
        index = 1
        for i in range(k):
            if flag:
                index+=1
            else:
                index-=1
            if index == n:
                flag = False
            if index == 1:
                flag = True
        return index-1
        