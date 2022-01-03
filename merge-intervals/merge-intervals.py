class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(intervals)<=1:
            return intervals
        sorted_intervals=sorted(intervals, key=lambda x:x[0])
        merged=[]
        start=sorted_intervals[0][0]
        end=sorted_intervals[0][1]
        for i in range(1,len(sorted_intervals)):
            if end<sorted_intervals[i][0]:
                merged.append([start,end]) 
                start=sorted_intervals[i][0] 
                end=sorted_intervals[i][1] 
            else: 
                end=max(end,sorted_intervals[i][1]) 
        merged.append([start,end]) 
        return merged
        