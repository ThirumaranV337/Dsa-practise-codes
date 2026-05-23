class Solution:
    def leastWeightCapacity(self, arr, D):
        low=max(arr)
        high=sum(arr)
        ans=0
        while low<=high:
            mid=(low+high)//2
            checker=self.find_capacity(arr,D,mid)
            if checker:
                
                ans=checker
                high=mid-1
            else:
                low=mid+1
        return ans
            
            
    def find_capacity(self,arr,D,capacity):
        d_count=0
        count=0
        for j in range(len(arr)):
            if arr[j]+count <= capacity:
                count+=arr[j]
            else:
                d_count+=1
                count=arr[j]
        d_count+=1
        count=arr[j]
        if d_count <= D:
           return capacity

