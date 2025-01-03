/**
 * @param {number[]} nums
 */
 var NumArray = function(nums) {
    this.size = nums.length;
    this.sumArray = new Array(nums.length + 1).fill(0);
    this.sumArray[0] = nums[0];

    for(let i = 1; i < this.size; i++){
        this.sumArray[i] = this.sumArray[i - 1] + nums[i];

    }
};

/** 
 * @param {number} left 
 * @param {number} right
 * @return {number}
 */
NumArray.prototype.sumRange = function(left, right) {
    if(left == 0){
        return this.sumArray[right]
    } else {
        return this.sumArray[right] - this.sumArray[left - 1];
    }
};

/** 
 * Your NumArray object will be instantiated and called as such:
 * var obj = new NumArray(nums)
 * var param_1 = obj.sumRange(left,right)
 */