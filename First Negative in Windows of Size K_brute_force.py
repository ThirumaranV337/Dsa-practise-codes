class Solution:
    def firstNegInt(self, arr, k): 
        neg_count=[]
        for i in range(len(arr)-k+1):
            for j in range(i,i+k):
                if arr[j]<0:
                    neg_count.append(arr[j])
                    break
            if arr[j]>=0:
                neg_count.append(0)
        return neg_count 
                
                
                    
                    
