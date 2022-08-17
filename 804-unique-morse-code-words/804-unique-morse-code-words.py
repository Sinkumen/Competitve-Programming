class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morses = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
 
        return len({"".join(morses[ord(char)-ord("a")] for char in word) for word in words})