class Solution:
    def findPages(self, arr, k):
        low=max(arr)
        high=sum(arr)
        ans=-1
        if len(arr)<k:
            return -1
        elif k==1:
            return high
        else:
            ##Binary search
            while low<=high:
                mid=(low+high)//2
                std_count=self.possible_page(arr,mid)
                if std_count<=k:
                    ans=mid
                    high=mid-1
                else:
                    low=mid+1
            
            return ans
    def possible_page(self,arr,i):
        std=1
        page_count=0
        for j in range(len(arr)):
            if arr[j]+page_count <=i:
                page_count+=arr[j]
            else:
                std+=1
                page_count=arr[j]
        return std
        

            
o1=Solution()
arr=[15 ,10 ,19 ,10 ,5 ,18 ,7]
k=5
ans=o1.findPages( arr, k)
