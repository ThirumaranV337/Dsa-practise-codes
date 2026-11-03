class Solution:
    def startStation(self, gas, cost):
        #  code here

        if sum(gas)<sum(cost):
            return -1
        current_gas=0
        current_index=0
        for i in range(len(gas)):
            current_gas+=gas[i]-cost[i]
            if current_gas<0:
                current_index=i+1
                current_gas=0
        return current_index 
            
                
            
