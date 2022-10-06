const PriorityQueue = function() {
    this.queue = []
    this.createItem = (item, priority) => {
        return { item, priority }
    }
    this.put = (node) => {
        if(this.queue.length === 0) {
            this.queue.push(node)
        } else {
            let isAdded = false
            for(let i = 0; i < this.queue.length; i++) {
                if(node.val < this.queue[i].val) {
                    this.queue.splice(i, 0, node)
                    isAdded = true
                    break;
                }
            }
           if(!isAdded) {
                this.queue.push(node)
            }
        }
    }
    this.dequeue = () => {
        return this.queue.shift()
    }
}
    

function mergeKLists(lists: Array<ListNode | null>): ListNode | null {
    const pq = new PriorityQueue()
    for(let i = 0; i < lists.length; i++) {
        let list = lists[i]
        while(list) {
            pq.put(list)
            list = list.next
        }
    }
    let first =  pq.dequeue()
    if(!first) {
        return null
    }
    let current = new ListNode(first.val)
    let prehead = new ListNode()
    prehead.next = current
    while(pq.queue.length) {
        let item = pq.dequeue()
        current.next = new ListNode(item.val)
        current = current.next
    }
    return prehead.next
};