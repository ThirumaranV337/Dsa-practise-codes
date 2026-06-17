class Solution(object):
    def findKthNumber(self, m, n, k):
        low = 1
        high = m * n

        while low < high:
            mid = (low + high) // 2

            if self.position_checker(m, n, mid) < k:
                low = mid + 1
            else:
                high = mid

        return low

    def position_checker(self, m, n, mid):
        count = 0
        for i in range(1, m + 1):
            count += min(mid // i, n)
        return count
