class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        #int list nums
        
        n=list(set(nums))
        n.sort()
        if(len(set(nums))<3):
            return max(nums)
        return n[-3]