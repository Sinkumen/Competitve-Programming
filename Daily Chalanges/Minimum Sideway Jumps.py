class Solution:
    def minSideJumps(self, obstacles) -> int:
        memory = {}

        def findSideJumps(curLane, index):
            nonlocal memory
            if (curLane, index) in memory:
                return memory[(curLane, index)]
            if index == len(obstacles)-1:
                return 0
            if obstacles[index+1] != curLane:
                val = findSideJumps(curLane, index+1)
                memory[(curLane, index)] = val
                return val
            if obstacles[index+1] == curLane:
                if obstacles[index] == 0:
                    minJump = len(obstacles)
                    for lane in [1, 2, 3]:
                        if lane != curLane:
                            val = findSideJumps(lane, index+1)
                            minJump = min(minJump, val)
                    memory[(curLane, index)] = minJump + 1
                    return minJump + 1
                else:
                    minJump = len(obstacles)
                    for lane in [1, 2, 3]:
                        if lane != curLane and lane != obstacles[index]:
                            val = findSideJumps(lane, index+1)
                            memory[(curLane, index)] = val + 1
                            return val + 1

        return findSideJumps(2, 0)
