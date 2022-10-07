function permute(nums) {
  const result = [];
  const visited = new Set();
  dfs(nums, result, [], visited);
  return result;
};

function dfs(nums, result, permutation, visited) {
  if(permutation.length === nums.length){
    result.push([...permutation]);
    return;
  }
  
  for(let i = 0 ; i < nums.length ; i++){
    if(visited.has(i)) continue;
    

    permutation.push(nums[i]);
    visited.add(i);
    
    dfs(nums, result, permutation, visited);
    
    visited.delete(i);
    permutation.pop();
  }
}