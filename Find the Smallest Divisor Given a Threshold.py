import math
class Solution(object):
    def smallestDivisor(self, nums, threshold):
        maximum=max(nums)
        low=1
        high=maximum
        while low<=high:
            mid=(low+high)//2
            checker=self.div_sum(nums,mid)
            if checker<=threshold:
                ans=mid
                high=mid-1
            elif checker>threshold:
                low=mid+1
        return ans
        
    def div_sum(self,nums,mid):
        count=0
        for i in nums:
            count+=math.ceil(i/mid)
        return count
        

o1=Solution()
nums=[1,2,5,9]
thrs=6
ans=o1.smallestDivisor(nums,thrs)
