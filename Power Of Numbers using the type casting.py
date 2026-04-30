class Solution:
    def reverseexponentiation(self, n):
        string=str(n)
        reversed=string[::-1]
        integer=int(reversed)
        ans=n**integer
        return ans
        
