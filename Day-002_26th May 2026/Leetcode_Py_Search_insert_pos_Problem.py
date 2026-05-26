class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # sorted list nums
        # distinct integers
        # target int variable
        n = len(nums)
        x=[]
        ans = 0
        for i in range(n):
            if nums[i] == target:
                ans = i
        if(target not in nums):
            nums.append(target)
            nums.sort()
        y=len(nums)
        for i in range(0,y):
            if nums[i] == target:
                ans = i
        return ans