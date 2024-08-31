class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        maxval = max(nums)
        maxIndex = nums.index(maxval)
        nums.sort()
        if (nums[-2]*2)>nums[-1]:
            return -1
        else:
            return maxIndex
            

        