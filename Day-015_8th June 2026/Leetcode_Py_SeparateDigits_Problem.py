class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        ans=[]
        for i in nums:
            for j in range(len(str(i))):
                k=str(i)[j]
                ans.append(int(k))
        return ans
