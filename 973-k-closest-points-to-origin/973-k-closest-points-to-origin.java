class Solution {
    public int[][] kClosest(int[][] points, int k) {
    Queue<int[]> pq = new PriorityQueue<>((a,b) -> (a[0] - b[0]));
    
    
    for(int[] point : points){
        int[] entry = new int[]{distance(point[0], point[1]), point[0], point[1]};
        pq.offer(entry);
        
        
    }
    
    int[][] result  = new int[k][2];
    
    for(int i = 0; i < k; i++){
        
        int[] curr = pq.poll();
        result[i][0] = curr[1];
        result[i][1] = curr[2];
    }
    
    return result;
    
}

public int distance(int x, int y){
    return x*x + y*y;

}
}