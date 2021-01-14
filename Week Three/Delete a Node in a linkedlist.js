function removeNode(index) {
  node.data = node.next.data;
  node.next = node.next.next;
}
