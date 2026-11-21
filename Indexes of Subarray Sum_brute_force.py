class Solution:
    def subarraySum(self, arr: list[int], target: int) -> list[int]:
        # code here
        for i in range(len(arr)):
            if arr[i]==target:
                return [i+1,i+1]
            sum=0
            sum+=arr[i]
            for j in range(i+1,len(arr)):
                sum+=arr[j]
                if sum==target:
                    return [i+1,j+1]
            
        return [-1]
                
