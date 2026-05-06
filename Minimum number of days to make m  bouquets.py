class Solution(object):
    def minDays(self, bloomDay, m, k):
        length=len(bloomDay)
        possible=0
        minimum=min(bloomDay)
        maximum=max(bloomDay)
        pointer=minimum
        counter=0
        if m*k>length:
            return -1
        ##pointer within the possible range 
        while  pointer<=maximum:
            for i in range(0,length):## for loop to check all the value 
                if bloomDay[i]<=pointer:
                    counter+=1

                else:
                    poss_value=counter//k## checking the how many possible boke can make 
                    possible+=poss_value
                    counter=0
                if possible>=m:
                    return pointer
                if i==length-1:
                    poss_value=counter//k
                    possible+=poss_value
                    if possible>=m:
                        return pointer

                    counter=0
                    
            counter=0
            possible=0
            pointer+=1

            
o1=Solution()
arr=[7,7,7,7,12,7,7]
ans=o1.minDays(arr,2,3)
