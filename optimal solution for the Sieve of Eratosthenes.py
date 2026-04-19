class Solution:
    def sieve(self, n):
        Value="T"
        n+=1
        arr=[Value]*n
        arr[0]="F"
        arr[1]="F"
        temp=[]
        for i in range(2,int(n**0.5) + 1):
            if arr[i]=="T":
              #here I am using jumping the simple logic for example you are in 2 then the multiple of 2 is jump of 2
                for j in range(i*i,n,i):
                    arr[j]='F'
                        
        for k in range(n):
            if arr[k]=="T":
                temp.append(k)
        return temp
                
o1=Solution()
n=5
ans=o1.sieve(n)
