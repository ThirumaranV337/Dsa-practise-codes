class Solution:
    def binarySearch(self, arr, k):
        # 1. Find the bounds exponentially
        start = 0
        end = 1
        
        try:
            # We expand until we find a value >= k
            while arr[end] < k:
                size = end - start + 1
                start = end + 1
                end = end + size * 2
        except IndexError:
            # If we hit the end of the array, we don't know the exact size,
            # but we know 'end' is now past the limit.
            pass

        # 2. Binary Search within [start, end]
        left = start
        right = end
        
        while left <= right:
            mid = (left + right) // 2
            try:
                if arr[mid] == k:
                    return True
                elif arr[mid] < k:
                    left = mid + 1
                else:
                    right = mid - 1
            except IndexError:
                # If mid hits out of bounds, treat it as "too large" 
                # and move the right pointer in.
                right = mid - 1
                
        return False 

o1 = Solution()
arr = [1, 2, 3, 4, 6]
k = 6
