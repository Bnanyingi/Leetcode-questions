class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        #Length of the update array
        count = 0
        
        #Loop for all the elements in the array
        for i in range(len(nums)):
        
            if nums[i] != val:
                nums[count]=nums[i]
                count +=1
                return count