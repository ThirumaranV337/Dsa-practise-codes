class Solution:
    def longestSubarray(self, arr, k):
        # code here
        max_length=0
        hash_map={}
        hash_map[0]=-1
        
        pref_sum=0
        for i in range(len(arr)):
            
            pref_sum+=arr[i]
            
            prefsum_k=pref_sum-k
            if prefsum_k in hash_map:
                new_value=i-hash_map[prefsum_k]
                if new_value>=max_length:
                    max_length=new_value
            
            if pref_sum not in hash_map:
                hash_map[pref_sum]=i
            
            
        return max_length
                    
       
