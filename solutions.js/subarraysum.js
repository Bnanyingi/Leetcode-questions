// Given an array of integers nums and an integer k, return the total number of subarrays whose sum equals to k.

// A subarray is a contiguous non-empty sequence of elements within an array.

 

// Example 1:

// Input: nums = [1,1,1], k = 2
// Output: 2
// Example 2:

// Input: nums = [1,2,3], k = 3
// Output: 2




/**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */

//not an optimal solution - time complexity O(n2)
 var subarraySum = function(nums, k) {
    let count = 0;
    let n = nums.length;
    
 
 
    for(let i = 0; i < n; i++){
         let sum = 0
         for(let j = i; j < n; j++){
             sum += nums[j]
             if(sum === k){
                 count += 1
             }
         }
 
    }
 
    return count
 
 };



 //optimal solution
 /**
 * @param {number[]} nums
 * @param {number} k
 * @return {number}
 */
var subarraySum = function(nums, k) {
    let count = 0;
    let n = nums.length;
    let sum = 0;
    let prefix_sum = {0 : 1};
 
 
    for(i = 0; i < n; i++){
     sum += nums[i];
     let diff = sum - k;
     
     count += prefix_sum[diff] || 0;
     prefix_sum[sum] = (prefix_sum[sum] || 0) + 1;
      
    }
    return count
 
 };