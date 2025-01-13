
//Brute Force approach

//time complexity O(n*k)
//space complexity O(1)


function maxSum(arr, n, k){
    let max_sum = Number.MAX_SAFE_INTEGER;

    for(let i = 0; i < n - k + 1; i++){
        let current_sum = 0;
        for(let j = 0; j < k; j++){
            current_sum += arr[i + j];
        }

        max_sum = Math.max(current_sum, max_sum);
    }

    return max_sum;
}

// Driver code
const arr = [1, 4, 2, 10, 2, 3, 1, 0, 20];
const k = 4;
const n = arr.length;
console.log(maxSum(arr, n, k));



// Sliding Window 
//linear time complexity

function maxSubArraySum(nums, size) {
    if(size < 0 || size > arr1.length) return null;
    let currSum = 0;
    let maxSumSeen = -Infinity;
  
    for(let i = 0; i < nums.length; i++){
      currSum += nums[i];
      if(i >= size - 1){
        maxSumSeen = Math.max(currSum, maxSumSeen);
        currSum -= nums[i - (size - 1)];
  
      }
    }
    return maxSumSeen;
  }
  
  const arr1 = [1, 2, 3, 5, 4, 8, 6, 2];
  console.log(maxSubArraySum(arr1, 3));