class Solution:   
    def peakElement(self, arr):
        length=len(arr)
        if length==1:
            
            return 0
        elif arr[0]>arr[1]:
            return 0
        elif arr[length-1]>arr[length-2]:
            return length-1
        else:
            low=1
            high=length-2
            while low<=high:
                mid=(low+high)//2
                if arr[mid]>arr[mid-1] and arr[mid+1]<arr[mid]:
                    return mid
                elif arr[mid-1]<arr[mid]:
                    low=mid+1
                elif arr[mid-1]>arr[mid]:
                    high=mid-1
            return False
