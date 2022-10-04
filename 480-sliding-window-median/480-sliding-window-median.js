/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number[]}
 */
var medianSlidingWindow = function(nums, k) {
  const minHeap = new Heap();
  const maxHeap = new Heap(undefined, (a, b) => b - a);
  const answer = [];
  let count = 0;
  function makeBalance() {
    if(maxHeap.size > minHeap.size) {
      minHeap.add(...maxHeap.pop());
    }
    else if(minHeap.size - maxHeap.size > 1) {
      maxHeap.add(...minHeap.pop());
    }
  }
  
  for(let num of nums) {
    let top = minHeap.peek() == null? -Infinity: minHeap.peek();
    if(num >= top) {
      minHeap.add(num, count++);
    } else {
      maxHeap.add(num, count++);
    }
    makeBalance();
    if(maxHeap.size + minHeap.size == k) {
      if(k & 1) {
        answer.push(minHeap.peek());
      } else {
        answer.push( (minHeap.peek() + maxHeap.peek()) / 2);
      }
      let res = maxHeap.popAt(count - k);
      if(!res) {
        minHeap.popAt(count - k);
      }
      makeBalance();
    }    
  }
  return answer;
};

class Heap {
  constructor(array = [], cmpFn) {
    this.name = cmpFn == undefined? 'min': 'custom';
    this.cmpFn = cmpFn || this.internalCmpFn;
    this.tree = [];
    this.size = 0;
    this.count = 0;
    this.idxMap = new Map();
    this.idxRevMap = new Map();
    for(let value of array) {
      this.add(value);
    }
  }
  _left(idx) {
    return 2 * idx + 1;
  }
  _right(idx) {
    return 2 * idx + 2;
  }
  _parent(idx) {
    return (idx - 1) / 2 >> 0;
  }
  _swap(i, j) {
    let countI = this.idxMap.get(i);
    let countJ = this.idxMap.get(j);
    let idxI = this.idxRevMap.get(countI);
    let idxJ = this.idxRevMap.get(countJ);
    this.idxMap.set(i, countJ);
    this.idxMap.set(j, countI);
    this.idxRevMap.set(countI, j);
    this.idxRevMap.set(countJ, i);
    [this.tree[i], this.tree[j]] = [this.tree[j], this.tree[i]];
  }
  
  internalCmpFn(value1, value2) {
    return value1 - value2;
  }
  _heapifyUp(idx) {
    let parent = this._parent(idx);
     while(parent != idx && this.cmpFn(this.tree[idx], this.tree[parent]) < 0) {
      this._swap(idx, parent);
      idx = parent;
      parent = this._parent(idx);
    }
  }
  
  add(value, count) {
    count = count == undefined? this.count: count;
    this.tree[this.size] = value;
    this.idxMap.set(this.size, count);
    this.idxRevMap.set(count, this.size);
    let idx = this.size;
    this._heapifyUp(idx);
    this.size++;
    this.count++;
  }
  
  heapify(idx) {
    let left = this._left(idx);
    let right = this._right(idx);
    let current = idx;
    if(left < this.size && this.cmpFn(this.tree[left], this.tree[idx]) < 0) {
      current = left;
    }
    if(right < this.size && this.cmpFn(this.tree[right], this.tree[current]) < 0) {
      current = right;
    }
    if(current != idx) {
      this._swap(idx, current);
      this.heapify(current);
    }
  }
  
  pop() {
    if(this.size == 0) {
      return null;
    }
    let value = this.tree[0];
    let count = this.idxMap.get(0);
    this._swap(0, this.size - 1);
    this.size--;
    this.tree.length = this.size;
    this.heapify(0);
    this.idxRevMap.delete(count);
    this.idxMap.delete(this.size);
    return [value, count];
  }
  
  popAt(count) {
    if(!this.idxRevMap.has(count) || this.size == 0) {
      return null;
    }
    let idx = this.idxRevMap.get(count);
    let value = this.tree[idx];
    this._swap(idx, this.size - 1);
    this.size--;
    this.tree.length = this.size;
    this.heapify(idx);
    this._heapifyUp(idx);
    this.idxRevMap.delete(count);
    this.idxMap.delete(this.size);
    return [value, count];
  }
  
  peek() {
    return this.tree[0];
  }
}