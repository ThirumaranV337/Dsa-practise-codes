class Solution:
    def isBalanced(self, s):
        stack=[]
        checker=["{","[","("]
        checker_map=set(checker)
        for i in s:
            if i in checker_map:
                stack.append(i)
            elif i == "}" :
                if len(stack)>0:
                    stack_last=stack.pop()
                    if stack_last=="{":
                        pass
                    else:
                        return False
                else:
                    return False
            elif i=="]":
                
                if len(stack)>0:
                    stack_last=stack.pop()
                    if stack_last=="[":
                        pass
                    else:
                        return False
                else:
                    return False
            elif i==")":
                
                if len(stack)>0:
                    stack_last=stack.pop()
                    if stack_last=="(":
                        pass
                    else:
                        return False
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
                    
                
            
        
        
