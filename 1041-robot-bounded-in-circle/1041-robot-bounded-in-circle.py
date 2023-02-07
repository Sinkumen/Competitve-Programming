class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        direction = "N"
        lefts = {"N":"W","W":"S","S":"E","E":"N"}
        rights = {"N":"E","E":"S","S":"W","W":"N"}
        go = {"N":(0,1),"E":(1,0),"W":(-1,0),"S":(0,-1)}
        x,y = 0,0
        for step in instructions:
            if step == "L":
                direction = lefts[direction] 
            if step == "R":
                direction = rights[direction] 
            if step == "G":
                x += go[direction][0]
                y += go[direction][1]
        if direction == "N" and (x,y) != (0,0):
            return False
        return True

                