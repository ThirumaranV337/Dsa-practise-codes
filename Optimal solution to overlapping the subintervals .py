class Solution(object):
    def merge(self, intervals):
        sorted_intervals=sorted(intervals,key=lambda x:(x[0],x[1]))
        intervals_length=len(intervals)
        future_value=sorted_intervals[0]
        temp=[]
        for traverser in range(1,intervals_length):

            if future_value[1]>=sorted_intervals[traverser][0]:
                if future_value[1]>=sorted_intervals[traverser][1]:
                   pass
                else:
                   future_value[1]=sorted_intervals[traverser][1]
            else:
                temp.append(future_value)
                future_value=sorted_intervals[traverser]
        if future_value not in temp:
            temp.append(future_value)
        return temp
object=Solution()

arr=[[1,3],[2,6],[8,10],[15,18]]
ans=object.merge(arr)
