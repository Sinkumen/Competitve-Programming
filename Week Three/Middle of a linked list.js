var middleNode = function (head) {
  var fast = head;
  var slow = head;

  while (fast && fast.next !== null) {
    fast = fast.next.next;
    slow = slow.next;
  }

  return slow;
};
