class Solution:
    def prevSmaller(self, arr):
        # code here
        stack = []
        ans = []
        for i in arr:
            if len(stack) == 0:
                ans.append(-1)
                stack.append(i)
            elif i>stack[-1]:
                ans.append(stack[-1])
                stack.append(i)
            elif i <= stack[-1]:
                while len(stack) != 0 and i <= stack[-1]:
                    stack.pop()
                if len(stack) == 0:
                    ans.append(-1)
                    stack.append(i)
                elif i > stack[-1]:
                    ans.append(stack[-1])
                    stack.append(i)
        return ans
