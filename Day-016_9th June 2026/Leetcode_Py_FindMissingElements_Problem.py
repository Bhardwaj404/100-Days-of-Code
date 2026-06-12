class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        l=[]
        nums.sort()
        d=max(nums)-min(nums)+1
        if len(nums)==d:
            return l
        for i in range(min(nums),max(nums)+1):
            if i not in nums:
                l.append(i)
        return l
