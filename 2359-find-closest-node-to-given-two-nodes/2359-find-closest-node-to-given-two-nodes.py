class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        one = set()
        idx1 = defaultdict(int)
        idx2 = defaultdict(int)
        two = set()
        visited1 = set()
        visited2 = set()
        count = 0
        while node1 != -1:
            if node1 not in visited1:
                one.add(node1)
                idx1[node1] = count
                visited1.add(node1)
                node1 = edges[node1]
                count += 1
            else:
                node1 = -1
        count = 0
        while node2 != -1:
            if node2 not in visited2:
                two.add(node2)
                idx2[node2] = count
                visited2.add(node2)
                node2 = edges[node2]
                count += 1
            else:
                node2 = -1
      
        ans = -1
        order = float("inf")
        for node in one:
            if node in two:
                cur = max(idx1[node],idx2[node])
                if order > cur:
                    ans = node
                    order = cur
                elif order == cur and node < ans:
                    ans = node    
        return ans
       
               