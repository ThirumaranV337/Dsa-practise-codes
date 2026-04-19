class Solution:
    def sieve(self, n):
        temp=[]
        arr=[i for i in range(2,n+1)]
        for j in arr:
            
            
            temp.append(j)
            for k in arr:
                if k %j==0 and j!=k:
                    arr.remove(k)
        return temp
o1=Solution()
n=5
ans=o1.sieve(n)
