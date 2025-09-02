"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 
示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""

# 思路：
    # 先对intervals按照左端点进行排序。
    # 然后遍历排序后的区间，如果当前区间的左端点大于上一个区间的右端点，则说明没有重叠，可以直接添加到结果中。
    # 如果当前区间的左端点小于等于上一个区间的右端点，则说明有重叠，需要合并区间，将上一个区间的右端点更新为当前区间的右端点和上一个区间的右端点中的较大值。
    
from typing import List
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # 按照左端点排序
        intervals.sort(key=lambda x: x[0])
        res = []
        for interval in intervals:
            # 如果结果为空，或者当前区间的左端点大于上一个区间的右端点，则直接添加当前区间
            if not res or interval[0] > res[-1][1]:
                res.append(interval)
            else:
                # 否则有重叠，更新上一个区间的右端点
                res[-1][1] = max(res[-1][1], interval[1])
                
        return res
        