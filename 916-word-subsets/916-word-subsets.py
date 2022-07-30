class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        word2Dict = defaultdict(int)
        count = 0
        for word2 in words2:
            temp = defaultdict(int)
            for char in word2:
                temp[char] += 1
                if temp[char] > word2Dict[char]:
                    count+=1
                    word2Dict[char] += 1
        
        ans = []
        for word1 in words1:
            found = 0
            word1Dict = defaultdict(int)
            for char in word1:
                if char in word2Dict:
                    word1Dict[char] += 1
                    if word1Dict[char] <= word2Dict[char]:
                        found += 1
            if found == count:
                ans.append(word1)
        return ans