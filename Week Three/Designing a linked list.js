class Node {
  constructor(data, next = null) {
    this.data = data;
    this.next = next;
  }
}

class LinkedList {
  constructor() {
    this.head = null;
    this.size = 0;
  }

  insertAtFirst(data) {
    this.head = new Node(data, this.head);
    this.size++;
  }
  insertAtLast(data) {
    if (this.size === 0) {
      this.insertAtFirst(data);
    } else {
      let current = this.head;
      while (current.next) {
        current = current.next;
      }
      current.next = new Node(data);
    }
    this.size++;
  }

  insertAtIndex(data, index) {
    if (index > 0 && index > this.size) {
      return;
    }

    if (this.size === 0) {
      this.insertAtFirst(data);
    } else {
      let count = 0;
      let current = this.head;
      let previous;
      while (count < index) {
        previous = current;
        current = current.next;
        count++;
      }
      previous.next = new Node(data, current);
      this.size++;
    }
  }

  removeAtIndex(index) {
    if (index > 0 && index > this.size) {
      console.log("outofrange");
      return;
    }

    if (index === 0) {
      this.head = this.head.next;
    } else {
      let current = this.head;
      let previous;
      let count = 0;
      while (count < index) {
        count++;
        previous = current;
        current = current.next;
      }
      previous.next = current.next;
    }
    this.size--;
  }

  getAtIndex(index) {
    console.log("size", this.size);
    if (index > 0 && index >= this.size) {
      return;
    }
    if (index === 0) {
      return this.head ? this.head.data : null;
    } else {
      let current = this.head;
      let count = 0;
      while (count < index) {
        current = current.next;
        count++;
      }
      return current.data;
    }
  }

  reverse() {
    if (this.size <= 0) {
      return;
    } else {
      let previous = null;
      while (this.head) {
        let next = this.head.next;
        this.head.next = previous;
        previous = this.head;
        this.head = next;
      }
      this.head = previous;
    }
  }

  swap(index1, index2) {
    let max = index1 > index2 ? index1 : index2;
    let current = this.head;
    let previous1, previous2;
    let atIndex1, atIndex2;
    let count = 0;
    while (count < max) {
      if (count < index1) {
        previous1 = current;
        atIndex1 = current.next;
      }
      if (count < index2) {
        previous2 = current;
        atIndex2 = current.next;
      }
      current = current.next;
      count++;
    }
    previous1.next = atIndex2;
    previous2.next = atIndex1;
    let temp = atIndex1.next;
    atIndex1.next = atIndex2.next;
    atIndex2.next = temp;
  }

  printListData() {
    let current = this.head;
    while (current) {
      console.log(current.data);
      current = current.next;
    }
  }
}

const linkedList = new LinkedList();

linkedList.insertAtFirst(1);
linkedList.insertAtFirst(2);
linkedList.insertAtLast(3);
linkedList.insertAtLast(4);
linkedList.insertAtIndex(5, 1);

linkedList.printListData();
console.log("-----------------------");
linkedList.swap(1, 2);
linkedList.printListData();
