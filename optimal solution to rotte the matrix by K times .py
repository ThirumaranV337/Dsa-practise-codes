class Solution:
    def rotateMatrix(self, k, mat):
        if not mat or not mat[0]:
            return mat
            
        row = len(mat)
        col = len(mat[0])
        k = k % col
        
        for i in range(row):
            for _ in range(k):
                val = mat[i].pop(0) 
                mat[i].append(val)  
        return mat
o1 = Solution()
k = 1
mat = [[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]
ans = o1.rotateMatrix(k, mat)
