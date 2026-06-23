class Solution: 
    def selectionSort(self, arr):
        for i in range(len(arr)):
            min=float("inf")
            index=None
            for j in range(i,len(arr)):
                if arr[j]<min:
                    min=arr[j]
                    index=j
            arr[i],arr[index]=arr[index],arr[i]
        return arr
