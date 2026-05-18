class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        max_possible_dist = stalls[-1] - stalls[0]
        low=0
        high=max_possible_dist
        while low<=high:
            mid=(low+high)//2
            
            checker=self.ispossible(stalls,mid,k)
            if checker==True:
                low=mid+1
            else:
                high=mid-1
        return high
        return max_possible_dist 
    def ispossible(self,arr,index,k):
        count_cows=1
        last=arr[0]
        for i in range(1,len(arr)):
            if (arr[i]-last)>=index:
                count_cows+=1
                last=arr[i]
        if count_cows >= k:
            return True
        else:
            return False
    
        
