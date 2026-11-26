class Solution:
    def findSubString(self, s):
        # code here
        set_s=set(s)
        min_length=float("inf")
        for i in range(len(s)):
            sub_str=""
            for j in range(i,len(s)):
                sub_str+=s[j]
                if len(sub_str)<len(set_s):
                    continue
                else:
                    count=0
                    for k in set_s:
                        if k in sub_str:
                            count+=1
                        else:
                            break
                    if count+1>=len(sub_str):
                        if min_length > len(sub_str):
                            min_length=len(sub_str)
        return min_length
                    
        
    
    
