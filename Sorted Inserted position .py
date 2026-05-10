class Solution:
    def searchInsertK(self, arr, k):
        import bisect
        ans=bisect.bisect_left(arr, k)
        return ans
        
