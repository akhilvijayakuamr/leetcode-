class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        comb = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        if not digits:
            return []

        res=[""]
        for digit in digits:
            newres=[]
            for pre in res:
                for let in comb[digit]:
                    newres.append(pre+let)
            res = newres
        return res


        