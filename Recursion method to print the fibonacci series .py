class Solution:
    def nthFibonacci(self, n: int):
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            return self.nthFibonacci(n-1)+self.nthFibonacci(n-2)
        print(n)
    
        
