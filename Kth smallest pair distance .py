class Solution(object):
    def smallestDistancePair(self, nums, k):
        nums.sort()#"""Sorting to find the minimum and the maximu value ,and for using the sliding window inside the binary #search"""
        low=float('inf')#setting the float to infinity to find the minimum value 
        for i in range(1,len(nums)):##for used to traverse to find the minimum value 
            if nums[i]-nums[i-1] <low:#camparing the minimum greater curr low
                low=nums[i]-nums[i-1]
        high=nums[-1]-nums[0]#high possible spaces is max_value - min_value
        ## using the binary search 
        while low<high:##here we are not using the traditional low<=high because it will lead to the infinte loop due to infinite loop 
            mid=(low+high)//2
            no_values=self.checker(nums,mid)
            if no_values<k:
                low=mid+1
            else:
                high=mid#Can I find an even smaller distance that also satisfies the condition? ,and mid could be the answer
        return low#is the smallest value that has not been proven too small.
    def checker(self,arr,mid):
        ##applying the two pointer inside the binary search
        j=0
        count=0
        for i in range(1,len(arr)):
            while arr[i]-arr[j]>mid:##moving the left pointer
                j+=1
            count+=i-j
        return count
o1=Solution()
nums=[1,3,1]
k=1
ans=o1.smallestDistancePair(nums,k)

"""
intution:
We are checking whether the expected shortest distance (answer) could be mid.
"""
