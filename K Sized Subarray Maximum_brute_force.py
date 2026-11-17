class Solution:
    def maxOfSubarrays(self, arr, k):
        # code here
        if k==1:
            return arr
        initial_window=[]
        for i in range(k):
            initial_window.append(arr[i])
            
            
            
        max_element=[]
        max_element.append(max(initial_window))
        
        for j in range(k,len(arr)):
            initial_window.pop(0)
            initial_window.append(arr[j])
            max_element.append(max(initial_window))
        return max_element
o1=Solution()
ans=o1.maxOfSubarrays([1, 2, 3, 1, 4, 5, 2, 3, 6],3)


            
            
            
