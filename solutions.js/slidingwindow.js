
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

function maxSum1(arr, n, k){
    let max = 0;
    let sum = 0;

    for(let i = 0; i < k; i ++){
        sum += arr[i];
        max = sum;
     
    }

    for(let i = k; i < n; i++){
        sum += arr[i] - arr[i - k];
        if(sum > max){
            max = sum;
        }
    }

    return max;
}


let arr = [1, 4, 2, 10, 2, 3, 1, 0, 20];
let k = 4;
let n = arr.length;
document.write(maxSum1(arr, n, k));