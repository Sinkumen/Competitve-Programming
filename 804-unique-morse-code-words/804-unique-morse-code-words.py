class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        group = set()
        for word in words:
            morse = []
            for char in word:
                morse.append(morses[ord(char)-ord("a")])
            group.add("".join(morse))
        return len(group)
