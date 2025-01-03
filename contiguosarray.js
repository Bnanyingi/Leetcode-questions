// Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.

 

// Example 1:

// Input: nums = [0,1]
// Output: 2
// Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
// Example 2:

// Input: nums = [0,1,0]
// Output: 2
// Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.

// Solution
// 1.we are going to use hash map  to store the count of 0 and 1
//         2.we are going to declare a variable max_len and count assign it to 0
//         3.we are going to use a for loop to iterate through the array
//         4.if the current number is 0 then we will decrement the count by 1
//         5.if the current number is 1 then we will increment the count by 1
//         6. we are going to check that our count is equal to 0  are not if it 0 then we will make our max_len equal to i+1 .let me explain you why so keep following the logic 😄.

//         7. we are going to update our count to our hash .if it was already in the hash we will compare the value of the hash with max_len and if it is greater than max_len then we will update max_len to the value of the hash
//         if it was not there we will add the count to the hash
//             key --> count
//             value --> index
//         8. we are going to return max_len

//         let me break down the logic 
//                 hash={}
//                 max_len=0
//                 count=0
//                 nums=[0,1,1,0,1,1]

//                 our loop starts 
//                 first iteration:
//                     i=0
//                     current_num=nums[i] -->0
//                     here our current_num is 0 so count=count-1
//                     count=-1
//                     -1 is not in our hash so we are going to add in our hash
//                     hash={ '-1': 0 }
//                 second iteration:
//                     i=1
//                     count=-1
//                     current_num=nums[i] -->1
//                     here our current_num is 1 so count=count+1
//                     count=-1+1 = 0
//                     --> we got our count is equal to 0 so we will update our max_len to i+1 so max_len is 2
//                          let me explain you why :
//                             initially we declared our count to 0
//                             we will increment our count when current_num is 1 and decrement when current_num is 0
//                             then will update our max_len to i+1
//                         Note:
//                             when even we get out count is equal to 0 it mean we have equal number of 0 and 1
//                     0 is not in our hash so we are going to add in our hash
//                     hash={ '0': 1, '-1': 0 }

/**
 * @param {number[]} nums
 * @return {number}
 */
 var findMaxLength = function(nums) {
    const hash = {};
    let max_length = 0;
    let count = 0;
    for (let i = 0; i < nums.length; i++) {
      const current = nums[i];
      if (current === 0) {
          // if the current element is 0, then we decrement the count
        count--;
      } else if (current === 1) {
          // if the current element is 1, then we increment the count
        count++;
      }
  
      if (count === 0) {
          // if the count is equal to o then we have a contiguous subarray of length equal to i+1
        max_length = i + 1;
      }
      if (count in hash) {
      
        max_length = Math.max(max_length, i - hash[count]); // update our max length
      } else {
        hash[count] = i;
      }
  
    }
    return max_length;
  };