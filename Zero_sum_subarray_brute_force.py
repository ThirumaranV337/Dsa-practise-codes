class Solution:
    def subArrayExists(self, arr):
        # code here
        for i in range(len(arr)):
            sum_arr=[]
            for j in range(i,len(arr)):
                sum_arr.append(arr[j])
                if sum(sum_arr)==0:
                    return True
        return False
    
