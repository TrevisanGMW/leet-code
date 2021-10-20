/**
 * https://leetcode.com/problems/two-sum/
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function (nums, target) {
  let numbers = new Map();

  for (i = 0; i < nums.length - 1; i++) {
    pair_num = target - nums[i];

    if (numbers.has(pair_num)) {
      return [numbers.get(pair_num), i];
    }
    numbers.set(nums[i], i);
  }

  return numbers;
};

// Local Test
//let output = twoSum([2,7,11,15], 9);
//let output = twoSum([3,2,4], 6);
//console.log(output);

// Results
// 73.97% - 08/18/2021 16:23	Accepted	76 ms	41.2 MB	javascript
// Solution: Hashmaps
