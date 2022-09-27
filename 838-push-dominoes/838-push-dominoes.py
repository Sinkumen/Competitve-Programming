class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        final = ["."for _ in range(len(dominoes))]
        def cascade(i):
            nonlocal final
            l = i+1
            count = 0
            found = False
            while dominoes[i] != "R" and i >= 0:
                if dominoes[i] == "L":
                    found = True
                    break
                count += 1
                i -= 1
            if found:
                for j in range(i,l):
                    final[j] = "L"
            elif i < 0:
                for j in range(l):
                    final[j] = "L"
            else:
                half = count//2
                add = 1
                for j in range(half):
                    final[i+add] = "R"
                    final[l-add] = "L"
                    add += 1
                if (l-half) - (i+half) > 1:
                    final[i+half+1] = "."
        rightActive = False
        for i in range(len(dominoes)):
            if dominoes[i] == "L":
                rightActive = False
                final[i] = "L"
                cascade(i-1)
            elif rightActive or dominoes[i] == "R":
                rightActive = True
                final[i] = "R"
                

        return "".join(final)
            
            