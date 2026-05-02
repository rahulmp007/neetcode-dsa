class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        for (var i = 0; i < nums.length; i++) {
    
    for (var j = i; j < nums.length - 1; j++) {
      if (nums[i] + nums[j + 1] == target) {
        return [ i,j+1];
      }
    }
  }
  
}
}
