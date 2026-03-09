class Solution:
    def maxSubarraySum(self, arr):
        maximum_sum_value=None
        length_arr=len(arr)
        sum=0
        for i in range(length_arr):
            sub_arr=[]
            for j in range(i,length_arr):
                value_appending=arr[j]
                sub_arr.append(value_appending)
                max_temp=0
                for k in sub_arr:
                    max_temp+=k
                if maximum_sum_value is None:
                    maximum_sum_value=max_temp
                elif max_temp>maximum_sum_value:
                    maximum_sum_value=max_temp
        return maximum_sum_value
                    
object1=Solution()
arr=[-8,-3,-25,0,-9]
ans=object1.maxSubarraySum(arr)
print(ans)
