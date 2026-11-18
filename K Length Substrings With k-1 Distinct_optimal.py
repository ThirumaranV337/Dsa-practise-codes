class Solution:
    def substrCount(self, s, k):
        # code here
        count=[]
        ##setting the initial_window
        window=""
        for i in range(k):
            window+=s[i]
        count.append(len(set(window)))
        for j in range(k,len(s)):
            window=window[1:]+s[j]
            count.append(len(set(window)))
        count_value=0
        for l in count:
            if l==k-1:
                count_value+=1
        return count_value
            
            
            
