class Solution:
    def inversionCount(self, arr):
        array_length=len(arr)
        pair_count=0
        for traverser_1 in range(array_length):
            for traverser_2 in range(traverser_1,array_length):
                if arr[traverser_1] >arr[traverser_2]:
                    pair_count+=1
                
        return pair_count
o1=Solution()
arr=[2,4,1,3,5]
ans=o1.inversionCount(arr)
