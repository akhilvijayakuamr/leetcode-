class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        for i in arr:
            if(arr.count(i) != target.count(i)):
                return False
        return True
        