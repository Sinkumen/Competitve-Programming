var mergeTrees = function (t1, t2) {
  if (!t1 && !t2) {
    return null;
  }

  if (t1 && t2) {
    t1.val = t1.val + t2.val;
  }

  if (!t1 && t2) {
    return t2;
  }
  if (t1 && !t2) {
    return t1;
  }
  if (t1.left && t2.left) {
    mergeTrees(t1.left, t2.left);
  } else if (!t1.left && t2.left) {
    t1.left = t2.left;
  }

  if (t1.right && t2.right) {
    mergeTrees(t1.right, t2.right);
  } else if (!t1.right && t2.right) {
    t1.right = t2.right;
  }
  return t1;
};
