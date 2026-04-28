class Solution:
    def matrixDiagonally(self,mat):
        i=0
        j=0
        n=len(mat)
        ans=[]
        count=0
        up=1#flag to notice up or down 
        while count<n*n:
            if up==1:#checking the flag to upward direction 
                while i>=0 and j<n:## checking the condition that the upward move element 
                    ans.append(mat[i][j])
                    count+=1
                    if j==n-1:#first want to check this 
                        i+=1#this is important 
                        break
                    if i==0:
                        j+=1
                        break
                    
                    i-=1
                    j+=1
                up=0
            elif up==0:
                while j>=0 and i<n:
                    ans.append(mat[i][j])
                    count+=1
                    if i==n-1:
                        j+=1
                        break
                    
                    if j==0:
                        i+=1
                        break
                    i+=1
                    j-=1
                up=1
        return ans
o1=Solution()
mat=[[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]
ans=o1.matrixDiagonally(mat)
