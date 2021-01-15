var isPalindrome = function (head) {
  let str = generateStringFromList(head);
  let strReversed = generateStringFromList(reverseList(head));

  return str === strReversed;
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

var generateStringFromList = (head) => {
  if (!head) {
    return "";
  }
  let vals = [];
  let current = head;
  while (current) {
    vals.push(current.val);
    current = current.next;
  }
  return vals.join("");
};
