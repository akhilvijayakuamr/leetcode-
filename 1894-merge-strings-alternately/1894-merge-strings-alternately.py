class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s =[]
        i = 0
        while(i<=len(word1)-1 or i<=len(word2)-1):
            print(i)
            if i<=len(word1)-1:
                s.append(word1[i])
            if i<=len(word2)-1:
                s.append(word2[i])
            i+=1
        return ''.join(s)

        