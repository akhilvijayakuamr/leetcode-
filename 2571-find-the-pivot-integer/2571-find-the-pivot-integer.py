class Solution:
    def pivotInteger(self, n: int) -> int:
        i=1
        j=n
        val1=0
        val2=0
        while(i!=j):
            if(val1<val2):
                val1 += i
                i+=1
            else:
                val2 += j
                j-=1
        print(val1, val2)
        if(val1 == val2):
            return i
        else:
            return -1
        