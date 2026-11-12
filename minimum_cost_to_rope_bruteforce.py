class Solution:
    def minCost(self, arr):
        # code here
        minimum_cost=0
        while len(arr)>1:
            min_1=min(arr)
            arr.remove(min_1)
            min_2=min(arr)
            arr.remove(min_2)
            cost=min_1+min_2
            arr.append(cost)
            minimum_cost+=cost
        return minimum_cost
            
            
        
