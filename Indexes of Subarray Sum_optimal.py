class Solution:
    def subarraySum(self, arr: list[int], target: int) -> list[int]:
        # code here
        
        left=0
        right=0
        sum_value=arr[right]
        
        while right<len(arr):##using this because right is always move untill end so just want twant to make sure it is not exceeexceds its limit
            if sum_value==target:
                return [left+1,right+1]
            elif sum_value<target:
                
                right+=1
                if right<len(arr):
                    
                  sum_value+=arr[right]
            else:
                if left==right:
                    left+=1
                    right+=1
                    if right<len(arr):
                        sum_value=arr[right]
                    continue
                if sum_value>target:     
                    sum_value-=arr[left]
                    left+=1
        return [-1]
                


o1=Solution()
ans=o1.subarraySum([1, 2, 3, 7, 5],12)
