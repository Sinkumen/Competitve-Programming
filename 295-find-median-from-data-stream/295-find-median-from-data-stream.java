class MedianFinder {
    PriorityQueue<Integer> maxheap=new PriorityQueue<>((a,b)->b-a);
    PriorityQueue<Integer> minheap=new PriorityQueue<>();

    public void addNum(int num) {
        if(maxheap.isEmpty()||maxheap.peek()>=num)
        {
            maxheap.offer(num);
        }
        else{
            minheap.offer(num);
        }


        if(maxheap.size()<minheap.size())
        {
            maxheap.offer(minheap.poll());
        }
        else if(maxheap.size()>minheap.size()+1){
            minheap.offer(maxheap.poll());

        }

    }

    public double findMedian() {
        if(maxheap.size()==minheap.size())

        {
            return((maxheap.peek()+minheap.peek())/2.0);
        }
        return maxheap.peek();
    }
}