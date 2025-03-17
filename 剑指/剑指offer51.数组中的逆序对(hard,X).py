"""
在股票交易中，如果前一天的股价高于后一天的股价，则可以认为存在一个「交易逆序对」。
请设计一个程序，输入一段时间内的股票交易记录 record，返回其中存在的「交易逆序对」总数。

示例 1：

输入：record = [9, 7, 5, 4, 6]
输出：8
解释：交易中的逆序对为 (9, 7), (9, 5), (9, 4), (9, 6), (7, 5), (7, 4), (7, 6), (5, 4)。

这个题挨个两个比对timeout，因为record(0,50000)
"""

# 思路：在归并排序的合并（排序）阶段，本质就是两辆统计比较逆序对的个数，然后进行排序

from typing import List

class Solution:
    def reversePairs(self, record: List[int]) -> int:
        global res  # 声明全局变量 res
        res = 0  # 重新初始化 res，防止多次调用时错误累积
        
        def merge_sort(arr):
            global res  # 确保在 merge 里修改的是全局变量
            if len(arr) <= 1:
                return arr
            
            mid = len(arr) // 2
            left = merge_sort(arr[:mid])  # 递归左半部分
            right = merge_sort(arr[mid:])  # 递归右半部分
            
            return merge(left, right)  # 归并并统计逆序对
        
        def merge(left, right):
            global res  # 确保 res 正确修改
            temp = []
            i, j = 0, 0

            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    temp.append(left[i])
                    i += 1
                else:
                    temp.append(right[j])
                    res += len(left) - i  # 统计逆序对数量
                    j += 1
            
            temp += left[i:]  # 添加剩余左边元素
            temp += right[j:]  # 添加剩余右边元素
            
            return temp
        
        merge_sort(record)  # 执行归并排序并统计逆序对
        return res  # 返回最终逆序对数量

                