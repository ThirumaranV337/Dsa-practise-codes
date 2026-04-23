class Solution:
    def minRow(self,a):
        min=0
        row=1
        for i in range(len(a)):
            count=0
            for j in range(len(a[0])):
                if a[i][j]==0:
                    count+=1
            if count>min:
                min=count
                row=i+1
            
        return row
o1=Solution()
matrix=[[1, 1, 1, 1], [1, 1, 0, 0], [0, 0, 1, 1], [1, 1, 1, 1]]
ans=o1.minRow(matrix)
