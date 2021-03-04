class Solution:
    def findCircleNum(self, isConnected) -> int:
        visited = []
        province = 0
        for i in range(len(isConnected)):
            found = self.helper(isConnected[i], isConnected, visited, province)
            if found:
                province += 1
        return province

    def helper(self, city, isConnected, visited, province):
        found = False
        for i in range(len(city)):
            if city[i] == 1 and i not in visited:
                visited.append(i)
                found = True
                self.helper(isConnected[i], isConnected, visited, province)
        return found
