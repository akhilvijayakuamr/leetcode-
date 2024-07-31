class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count = 0
        cr = 0
        cl = 0
        for i in s:
            if (i=='R'):
                cr+=1
            else:
                cl+=1
            if(cl==cr):
                count+=1
                cl=0
                cr=0
        return count

        