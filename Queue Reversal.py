class Solution:
    def reverseQueue(self, q):
        # code here
        return_queue=[]
        for  i in range(len(q)):
            value=q.pop()
            return_queue.append(value)
        return q.extend(return_queue)
            
