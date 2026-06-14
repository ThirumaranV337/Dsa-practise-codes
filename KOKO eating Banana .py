class Solution(object):
    def minEatingSpeed(self, piles, h):
       import math
       left=1
       right=max(piles)
       capacity=0
       while left<=right:
            mid=(left+right)//2
            no_of_days=self.day_finder(mid,piles)
            if no_of_days <= h:
                capacity= mid
                right=mid-1
            elif no_of_days>h:
                left=mid+1
       return capacity
                
                
    def day_finder(self,weight,arr):
        total_weight=0
        for i in range(len(arr)):
            new_hours = math.ceil(float(arr[i]) / weight)
            total_weight+=new_hours
        return total_weight

o1=Solution()
arr= [3,6,7,11]
D=8
ans=o1.minEatingSpeed(arr,D)
