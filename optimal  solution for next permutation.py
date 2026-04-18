class Solution(object):
    def nextPermutation(self, nums):
       nums_length=len(nums)
       index=0
       if nums_length==1:
           return nums
       ##for finding the break point 
       for i in range(nums_length-2,-2,-1):
        if nums[i]<nums[i+1]:
            index=i
            break
       #if all are in sorted order then return the reverse
       if index == -1:
             
             return nums.reverse()
        #finding the element that suitable to swap with the break pointed element 
       for j in range(nums_length-1,index,-1):
            if nums[j]>nums[index]:
                #here we swaping the break point element with the suitable only once 
                nums[j],nums[index]= nums[index],nums[j]
                break
       #reversing the remaning after swapping          
       nums[index+1:]=reversed(nums[index+1:])
       return nums
o1=Solution()
nums=[3,2,1]
ans=o1.nextPermutation(nums)




        
        

            
