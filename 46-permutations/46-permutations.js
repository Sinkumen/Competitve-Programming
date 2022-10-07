function permute(nums) {
  const result = [];
  const visited = new Set();
  dfs(nums, result, [], visited);
  return result;
};

/*
  - permutation is used to keep track of current permutation
  - seen set is used to avoid using the same index twice
  - reuslt array is used to store the permutations
*/
function dfs(nums, result, permutation, visited) {
  if(permutation.length === nums.length){
    result.push([...permutation]);
    return;
  }
  
  for(let i = 0 ; i < nums.length ; i++){
    if(visited.has(i)) continue;
    
    // include the number at end of permutation
    permutation.push(nums[i]);
    visited.add(i);
    
    // continue dfs
    dfs(nums, result, permutation, visited);
    
    visited.delete(i);
    permutation.pop();
  }
}