class Solution:
    def countDistinct(self, arr, k):
        initial_window = set()
        unique_count = []

        for i in range(k):
            initial_window.add(arr[i])
        unique_count.append(len(initial_window))

        for j in range(k, len(arr)):
            # Only remove arr[j-k] if it is NOT present in the new window slice
            if arr[j-k] not in arr[j-k+1 : j+1]:
                initial_window.remove(arr[j-k])

            initial_window.add(arr[j])
            unique_count.append(len(initial_window))

        return unique_count

o1 = Solution()
ans = o1.countDistinct([1, 2, 1, 3, 4, 2, 3], 4)

