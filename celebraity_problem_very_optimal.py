
class Solution:
    def celebrity(self, mat):
        down=len(mat)-1
        top=0
        while top<down:
            if mat[top][down]==1:
                top+=1
            elif mat[down][top]==1:
                down-=1
            else:
                top+=1
                down-=1
        if top>down:
            return -1
        else:
            for i in range(len(mat)):
                if i!=top:
                    if mat[top][i]==0 and mat[i][top]==1:
                        continue
                    else:
                        return -1
            return top
                
