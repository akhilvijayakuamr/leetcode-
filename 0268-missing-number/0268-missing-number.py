class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        k=0
        nums.sort()
        print(nums)
        for i in nums:
            print(i)
            if(k!=i):
                return k
            else:
                k+=1
        return k

        