class Solution:
    def findSubString(self, s):
        # code here
        set_s=set(s)
        ##constructing the frequency array
        min_length=float("inf")
        string=""
        i=0
        for j in range(len(s)):

            string+=s[j]
            while i<=j and self.contains_s(string,set_s):
                new_length=j-i+1
                min_length=min(min_length,new_length)
                i+=1
                string=string[1:]
        return min_length

    def contains_s(self,string,set_s):
        for i in set_s:
            if i not in string:
                return False
        return True
