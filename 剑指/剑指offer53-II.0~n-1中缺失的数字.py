"""
某班级 n 位同学的学号为 0 ~ n-1。点名结果记录于升序数组 records。假定仅有一位同学缺席，请返回他的学号。

 

示例 1：

输入：records = [0,1,2,3,5]
输出：4
示例 2：

输入：records = [0, 1, 2, 3, 4, 5, 6, 8]
输出：7
"""

# 思路：二分查找，找到缺失的数字(核心思路：如果当前数字等于索引，说明缺失的数字在右边，否则在左边)
    # return left刚好能满足题目要求，因为left是第一个不满足条件的索引，即缺失的数字
class Solution:
    def takeAttendance(self, records: List[int]) -> int:
        left, right = 0, len(records) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if records[mid] == mid:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
