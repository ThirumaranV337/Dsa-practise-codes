class Solution:
    def insertionSort(self, arr):
        count=0
        for i in range(1,len(arr)):
            j=i
            while j>0 and arr[j]<arr[j-1]:
                arr[j],arr[j-1]=arr[j-1],arr[j]
                count+=1
                j-=1
        return arr,count
o1=Solution()
arr=[1,2,3,4,5]

ans=o1.insertionSort(arr)
print(ans)
