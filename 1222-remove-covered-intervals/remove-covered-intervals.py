class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        c=0
        for i in range(len(intervals)):
            for j in range(len(intervals)):
                if i==j:
                    continue
                if intervals[j][0]<=intervals[i][0] and intervals[i][1]<=intervals[j][1]:
                    c+=1
                    break
        return len(intervals)-c