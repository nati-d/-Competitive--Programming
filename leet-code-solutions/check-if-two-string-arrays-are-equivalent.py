class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1=""
        w2=""
        for i in range(len(word1)):
            w1+=word1[i]
        for i in range(len(word2)):
            w2+=word2[i]
        if w1 == w2:
            return True
        else:
            return False
        