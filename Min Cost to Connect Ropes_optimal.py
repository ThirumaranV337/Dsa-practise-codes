import heapq
class Solution:
    def minCost(self, arr):
        # code here
        minimum_cost=0
        heapq.heapify(arr)
        
        while len(arr)>1:
            min_1=heapq.heappop(arr)
            
            min_2=heapq.heappop(arr)
            cost=min_1+min_2
            heapq.heappush(arr,cost)
            minimum_cost+=cost
        return minimum_cost
        
        
            
            
        
