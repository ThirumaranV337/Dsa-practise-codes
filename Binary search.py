class Solution:
    def binarySearch(self, arr, k):
        low=0
        high=len(arr)-1
        while low<=high:
            mid=(low+high)//2
            if arr[mid]==k:
                return True
            elif arr[mid]<k:
                low=mid+1##avoid the unwanted value
            else:
                high=mid-1## avoid the unwanted value
        return False
o1=Solution()
arr=[1,2,3,4,6]
k=6
ans=o1.binarySearch(arr,k)
##Time complexity of this code is o(logn)
