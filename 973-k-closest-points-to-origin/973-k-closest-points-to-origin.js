class Heap {
    constructor(compareMethod) {
        this.heap = [];
        if (typeof compareMethod === 'function') {
            this._compare = compareMethod;
        }
    }
    
    _left(n) {
        return 2*n + 1;
    }
    
    _right(n) {
        return 2*n + 2;
    }
    
    // Returns index    
    _parent(n) {
        return Math.floor((n-1)/2);
    }
    
    _swap(n1, n2) {
        let temp = this.heap[n1];
        
        this.heap[n1] = this.heap[n2];
        this.heap[n2] = temp;
    }
    
    _isLeaf(n) {
        return typeof this.heap[this._left(n)] === 'undefined' && typeof this.heap[this._right(n)] === 'undefined';
    }
    
    
    _compare(val1, val2) {
        if (val1 < val2) {
            return 1;
        } else if (val1 > val2) {
            return -1;
        }
        return 0;
    }
    
    peek() {
        return this.heap[0];
    }
    
    push(newVal) {
        this.heap.push(newVal);
        let node = this.heap.length - 1;
        
        while(node > 0) {
            let parentIndex = this._parent(node);
            
            if (this._compare(this.heap[node], this.heap[parentIndex]) > 0) {
                this._swap(parentIndex, node)
                node = parentIndex;
            } else {
                break;
            }
        }
    }
    
    pop() {
        if (!this.heap.length) {
            return;
        }
        
        this._swap(0, this.heap.length - 1);
        let theGreatest = this.heap.pop();
        let nodeIndex = 0;
        
        while (!this._isLeaf(nodeIndex)) {
            let left = this._left(nodeIndex);
            let right = this._right(nodeIndex);
            
            let leftChild = this.heap[left];
            let rightChild = this.heap[right];
            
            if (typeof rightChild === 'undefined') {
                if (this._compare(leftChild, this.heap[nodeIndex]) > 0) {
                    this._swap(left, nodeIndex);
                }
                break;
            }
            
            if (this._compare(leftChild, rightChild) > 0 && this._compare(this.heap[nodeIndex], leftChild) < 0) {
                this._swap(nodeIndex, left);
                nodeIndex = left;
                continue;
            } else if (this._compare(rightChild, leftChild) >= 0 && this._compare(this.heap[nodeIndex], rightChild) < 0) {
                this._swap(nodeIndex, right);
                nodeIndex = right;
                continue;
            } else {
                break;
            }
        }
        
        return theGreatest;
    }
}

/**
 * @param {number[][]} points
 * @param {number} k
 * @return {number[][]}
 */
var kClosest = function(points, k) {
    let heap = new Heap((val1, val2) => {
        if (val1.distance < val2.distance) {
            return 1;
        } else if (val1.distance > val2.distance) {
            return -1;
        }
        return 0;
    });
    let output = [];
    
    for (point of points) {
        let distance = Math.sqrt(Math.pow(point[0], 2) + Math.pow(point[1], 2));
        let enchancedPoint = {
            point : point,
            distance: distance
        }
        
        heap.push(enchancedPoint); //O(logN)
    }
    
    for (let i = 0; i < k; i++) {
        output.push(heap.pop()['point']);
    }
    
    return output;
};