class Solution(object):
    def majorityElement(self, nums):
        length=len(nums)
        hash_map_count_storer={}
        for value_checker in nums:
            if value_checker in hash_map_count_storer:
                hash_map_count_storer[value_checker]+=1
            else:
                hash_map_count_storer[value_checker]=0
        majority_counter=max( hash_map_count_storer.values())
        for key , value in hash_map_count_storer.items():
            if value == majority_counter:
                majority_element=key
                break
        return majority_element
object1=Solution()
nums=[3,2,3]
ans=object1.majorityElement(nums)
#time complexity o(n)
#space complexity o(n)


                
