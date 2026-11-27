class Solution:
    def smallestSubstring(self, s):
        # code here
        curr_min_seize=float("inf")
        curr_window={"0":0,"1":0,"2":0}
        i=0
        for j in range(len(s)):
            curr_window[s[j]]+=1
            while i<=j and self.contains_012(curr_window):
                new_size=j-i+1
                curr_min_seize=min(curr_min_seize,new_size)
                curr_window[s[i]]-=1
                i+=1
                
        if curr_min_seize==float("inf"):
            return -1
        return curr_min_seize
        
    def contains_012(self,window):
        for value in "012":
            if window[value]==0:
                return False
        return True
                
                
