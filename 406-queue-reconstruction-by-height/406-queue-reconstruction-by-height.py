class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        def slide(start,amount):
            while amount and start < len(people)-1:
                people[start],people[start+1] = people[start+1],people[start]
                amount -= 1
                start += 1
        people.sort()
        
        for i in range(len(people)-1,-1,-1):
            cur,greater = people[i]
            temp = i-1
            while temp >= 0 and people[temp][0]==cur:
                greater -= 1
                temp -= 1
            slide(i,greater)
        return people
            
        