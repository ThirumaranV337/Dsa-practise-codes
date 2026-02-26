class Solution:
    def longestSubarray(self, arr, k):
        length_for_loop=len(arr)#this is for running for loop to traverse a full array
        hash_map={}#hash map to store the index and to find the oldest  index of the ckecker 
 
        sum=0#sum to store the current prefix sum
        max_length=0#used to store the max length
        for i in range(length_for_loop):#for loop to traverse a array
            sum+=arr[i]#performing the prefixsum
            if sum==k:# checking the presum ==k
                max_length=max(i+1,max_length)#finding the max length,here i+1 was used because the index start from 0
            if sum not in hash_map:#this line to avoid the over writing 
                hash_map[sum]=i#storing the index and the prefix sum
            checker=sum-k#here is the key concept ,that we are searching for the long size by removing the remaning
            if checker in hash_map:#here we finding the checker in hash for checking the index 
                new_length=i-hash_map[checker]#here we are storing the recent length
                max_length=max(new_length,max_length)#checking which length is longest 
        return max_length#finally returning the max length       
o1=Solution() 
arr=[10,5,2,7,1,-10]
k=15
ans=o1.longestSubarray(arr,k)
#the time comlexity is o(n)
#the space complexity is o(n)
