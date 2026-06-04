class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        #given an int array
        nums2=[]
        ans=[]
        nums2=nums[::-1]
        
        ans.extend(nums)
        ans.extend(nums2)
        return ans