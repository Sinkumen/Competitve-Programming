var removeElements = function (head, val) {
  if (!head || (!head.next && head.val === val)) {
    return null;
  }

  let current = head;
  let previous = null;
  if (head.val === val) {
  }
  while (current) {
    if (current === head && current.val === val) {
      head = head.next;
      current = head;
    } else {
      if (current.val === val) {
        previous.next = current.next;
        current = current.next;
      } else {
        previous = current;
        current = current.next;
      }
    }
  }
  return head;
};
