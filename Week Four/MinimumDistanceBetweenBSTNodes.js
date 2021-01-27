var minDiffInBST = function (root) {
  let nodes = [];
  inOrderTraversal(root, nodes);
  let min = nodes[1] - nodes[0];
  for (let i = 0; i < nodes.length; i++) {
    min =
      nodes[i + 1] && nodes[i + 1] - nodes[i] < min
        ? nodes[i + 1] - nodes[i]
        : min;
  }
  return min;
};

var inOrderTraversal = (root, nodes) => {
  if (root) {
    inOrderTraversal(root.left, nodes);
    nodes.push(root.val);
    inOrderTraversal(root.right, nodes);
  }
};
