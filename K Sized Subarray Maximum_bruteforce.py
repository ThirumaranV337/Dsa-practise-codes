class Solution:
    def maxOfMins(self, arr):
       # code here
       max_val=[]
       for i in range(1,len(arr)+1):
           value=self.minOfSubarrays(arr,i)
           max_val.append(value)
       return max_val
    
    def minOfSubarrays(self, arr, k)->set:
        # code here
        
            
        dequeue=[]
        min_element=[]
        for i in  range(k):
            if len(dequeue)==0:
                dequeue.append(arr[i])
            elif dequeue[-1]>arr[i]:
                while len(dequeue)>0 and dequeue[-1]>arr[i]:
                    dequeue.pop()
                dequeue.append(arr[i])
            else:
                dequeue.append(arr[i])
        min_element.append(dequeue[0])
        for j in range(k,len(arr)):
            if len(dequeue)==0:
                dequeue.append(arr[j])
            elif dequeue[-1]>arr[j]:
                while len(dequeue)>0 and dequeue[-1]>arr[j]:
                    dequeue.pop()
                dequeue.append(arr[j])
            elif dequeue[-1]<=arr[j]:
                dequeue.append(arr[j])
            if dequeue[0]==arr[j-k]:
                dequeue.remove(dequeue[0])
            min_element.append(dequeue[0])
        return max(min_element)
        
o1=Solution()
ans=o1.maxOfMins([10, 20, 30, 50, 10, 70, 30])
