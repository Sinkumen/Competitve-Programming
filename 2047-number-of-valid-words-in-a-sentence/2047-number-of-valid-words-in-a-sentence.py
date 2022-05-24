class Solution:
    def countValidWords(self, sentence: str) -> int:
        words = sentence.split()
        ans = 0
        for word in words:
            hyphen = (-1,0)
            punc = (-1,0)
            nonum = True
            last = 0
            for i in range(len(word)):
                char = word[i] 
                if char == "-":
                    hyphen = (i,hyphen[1]+1)
                elif char.isalpha():
                    last = i
                elif char.isnumeric():
                    nonum = False
                else:
                    punc = (i,punc[1]+1)
            
            if (0 < hyphen[0] < last <= len(word)-1 and hyphen[1] == 1 ) or  hyphen[0] == -1:
                if nonum and ((punc[0] == len(word)-1 and punc[1] == 1) or  punc[0] == -1):
                    ans += 1
        return ans