"""
给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。

请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

你必须设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1:

输入: [3,2,1,5,6,4], k = 2
输出: 5
示例 2:

输入: [3,2,3,1,2,4,5,5,6], k = 4
输出: 4

"""

# 思路：
    # 使用大小为k的小根堆，谁大就往堆插入，弹出堆顶元素，循环完后堆顶即为第k大元素
    # 时间复杂度 O(nlogk)
import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for x in nums:
            if len(heap) < k:
                heapq.heappush(heap, x)   # 先塞满 k 个
            else:
                if x > heap[0]:
                    heapq.heapreplace(heap, x)  # 更大就替换堆顶
        return heap[0]  # 堆顶即第 k 大
