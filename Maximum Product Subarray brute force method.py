class Solution:
    def maxProduct(self,arr):
        length_array=len(arr)
        if length_array==1:
            return arr[0]
        value_storer=[]
        for iterator1 in range(length_array):
            previous_value=arr[iterator1]
            value_storer.append( previous_value)
            for iterator2 in range(iterator1+1,length_array):
                adding_value=previous_value*arr[iterator2]
                value_storer.append(adding_value)
                previous_value=adding_value
        maximum_product=max(value_storer)
        return maximum_product
object1=Solution()
arr=[-1,2]
ans=object1.maxProduct(arr)


