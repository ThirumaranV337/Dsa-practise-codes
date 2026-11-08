class Solution:
    def firstNonRepeating(self, s):

        curr="#" ##used to maintain the current first non repeating
        string=""##used to store the returning answer
        queue=[]##used to track the next non repeating eligible character in queue order
        visited=[]###used to track the char is repeated or not 
        for i in s:
           if i in visited and i in queue:
               queue.remove(i)
           elif i not in visited:
               visited.append(i)
               queue.append(i)
           if len(queue)!=0:
               curr=queue[0]
           else:
               curr="#"
           string+=curr
        return string
o1=Solution()
ans=o1.firstNonRepeating("nnmmon")
