class Solution(object):
    def trap(self, height):
        length=len(height)
        test_pre_max=[]
        pre_max=[]
        for i in range(length):
            value=height[i]
            test_pre_max.append(value)
            max_element_preffix=max(test_pre_max)
            pre_max.append(max_element_preffix)
        test_suff_max=[]
        suff_max=[] 
        for j in range(length,0,-1):
            value=height[j-1]
            test_suff_max.append(value)
            max_element_suffix=max(test_suff_max)
            suff_max.append(max_element_suffix)
        pointer2=length
        sum=0
        for k in range(length):
            pointer2=length-1-k
            min_element=min(pre_max[k],suff_max[pointer2])
            adder=min_element-height[k]
            sum+=adder
        return sum
             
o1=Solution()
height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans=o1.trap(height)
#time complexity o(n)
