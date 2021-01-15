var reverseListRecursively = (head) => {
  if (!head || !head.next) {
    return head;
  }
  let reversed = reverseList(head.next);
  head.next.next = head;
  head.next = null;
  return reversed;
};

var reverseList = (head) => {
  if (!head || !head.next) {
    return head;
  }
  let previous = null;
  while (head) {
    let next = head.next;
    head.next = previous;
    previous = head;
    head = next;
  }

  return previous;
};
