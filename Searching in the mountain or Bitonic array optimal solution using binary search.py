class Solution:
    def solve(self, A, B):
        if not A:
            return -1
            
        peak_idx = self.findPeakElement(A)
        
        # 1. Search in the ascending part (0 to peak_idx)
        res = self.binary_search(A, B, 0, peak_idx, ascending=True)
        if res != -1:
            return res
            
        # 2. Search in the descending part (peak_idx + 1 to end)
        return self.binary_search(A, B, peak_idx + 1, len(A) - 1, ascending=False)

    def binary_search(self, arr, target, low, high, ascending):
        while low <= high:
            mid = (low + high) // 2
            if arr[mid] == target:
                return mid
            
            if ascending:
                if arr[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
            else: # Descending logic
                if arr[mid] > target:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1

    def findPeakElement(self, arr):
        n = len(arr)
        low, high = 0, n - 1
        
        while low < high:
            mid = (low + high) // 2
            # If the next element is greater, the peak is to the right
            if arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                # If the next element is smaller, mid could be the peak
                high = mid
        return low
