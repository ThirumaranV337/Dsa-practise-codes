class Solution(object):
    def findKthNumber(self, m, n, k):
        arr=[]
        for i in range(1,m+1):
            for j in range(1,n+1):
                arr.append( i*j)
        arr.sort()
        return arr[k-1]      
