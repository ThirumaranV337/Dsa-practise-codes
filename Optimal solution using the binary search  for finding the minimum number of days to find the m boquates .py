class Solution(object):
    def minDays(self, bloomDay, m, k):
        poss=0
        count=0
        low=min(bloomDay)
        high=max(bloomDay)
        ans=0
        if m*k > len(bloomDay):
            return -1
        while low<=high:
            mid=(low+high)//2
            checker=self.check_possibility(bloomDay,mid,k,m)
            if checker:
                ans=checker
                high=mid-1
            else:
                low=mid+1
        return ans
            
            
        
            
    def check_possibility(self,bloomDay,i,k,m):
        poss=0
        count=0
        for j in range(len(bloomDay)):
            if bloomDay[j]<=i:
                count+=1
            else:
                new_poss=count//k
                poss+=new_poss
            
                count=0
        new_poss=count//k
        poss+=new_poss
        count=0
        if poss>=m:
            return i
        poss=0

 
