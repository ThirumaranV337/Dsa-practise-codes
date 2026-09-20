class Solution:
    def nextGreaterElements(self, nums: list[int]) -> list[int]:
        stack=[]
        return_list=[]
        n=len(nums)
        start=2*n-1
      
        for i in range(start,-1,-1):
           
            if len(stack)==0:
                return_list.append(-1)
                stack.append(nums[i%n])
            elif nums[i%n]<stack[-1]:
                return_list.append(stack[-1])
                stack.append(nums[i%n])
            elif nums[i%n]>=stack[-1] :
                while len(stack)!=0 and nums[i%n]>=stack[-1]:
                    stack.pop()
                if len(stack)==0:
                    return_list.append(-1)
                    stack.append(nums[i%n])
                elif nums[i%n]<stack[-1]:
                    return_list.append(stack[-1])
                    stack.append(nums[i%n])


        reversed_list = return_list[::-1] 
        final_ans=reversed_list[:n]
        return final_ans
        
