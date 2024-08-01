class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count = 0
        for i in details:
            if 60<int(i[-4:-2]):
                count+=1
        return count
        