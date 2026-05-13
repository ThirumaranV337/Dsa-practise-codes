class Solution(object):
    def search(self, nums, target):
        left=0
        right=len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return True
            elif nums[left]==nums[mid] and nums[mid]==nums[right]:
                left+=1
                right-=1
                continue
            elif nums[left]<=nums[mid]:## we checking the right half is first sorted or not 
                if nums[left]<=target and nums[mid]>=target:## if the right half is sorted then we finding the target is falling the range or not 
                    right=mid-1#if it true skip the left side 
                else:
                    left=mid+1#if it is false skip the right side 
            else:##then came to here if the left is not sorted or the value are not in the range 
                if nums[mid]<=target and nums[right]>=target:## checking the target is falling inside the range or not 
                    left=mid+1##skipping the left side part 
                else:
                    right=mid-1##skipping the right side part
        return False
