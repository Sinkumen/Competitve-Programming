var insertionSortList = function (head) {
  if (!head || !head.next) {
    return head;
  }
  let sorted = null;
  let current = head;
  while (current) {
    let next = current.next;
    sorted = insertSortedList(sorted, current);
    current = next;
  }
  head = sorted;
  return head;
};

function insertSortedList(sortedHead, item) {
  if (!sortedHead || sortedHead.val >= item.val) {
    item.next = sortedHead;
    return item;
  } else {
    let current = sortedHead;
    while (current.next && current.next.val <= item.val) {
      current = current.next;
    }
    item.next = current.next;
    current.next = item;

    return sortedHead;
  }
}
