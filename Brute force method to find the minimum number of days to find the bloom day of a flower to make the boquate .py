class Solution(object):
    def minDays(self, bloomDay, m, k):
        poss=0
        count=0
        minimum=min(bloomDay)
        maximum=max(bloomDay)
        if m*k > len(bloomDay):
            return -1
        for i in range(minimum,maximum+1):
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
o1=Solution()  
arr=[7,7,7,7,12,7,7]
m=2
k=3
ans=o1.minDays(arr,m,k)   
