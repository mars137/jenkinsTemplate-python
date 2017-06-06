class Solution(object):
    def ArrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # your solution here
        
        #check if num is not present
        if not nums:
        	return
        
        nums.sort()
        sum=0

        for i in range(0,len(nums),2):
        	sum+=nums[i]	 
        return sum
