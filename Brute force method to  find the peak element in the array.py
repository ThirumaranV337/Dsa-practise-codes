class Solution:   
    def peakElement(self, arr):
        length=len(arr)
        if length==1:
            return 0
        
        for i in range(length):
            if i==0:
                if arr[i+1]<arr[i]:
                    return i
            elif i==length-1:
                if arr[i-1]<arr[i]:
                    return i
            else:
                if arr[i+1]<arr[i] and arr[i-1]<arr[i]:
                    return i
        return False
