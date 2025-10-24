"""
给你一个整数数组 nums 和一个整数 k ，请你返回其中出现频率前 k 高的元素。你可以按 任意顺序 返回答案。

示例 1：

输入：nums = [1,1,1,2,2,3], k = 2

输出：[1,2]

示例 2：

输入：nums = [1], k = 1

输出：[1]

你所设计算法的时间复杂度 必须 优于 O(n log n)
"""

# 思路：
    # 根据要求，设计堆的算法都是logk的时间复杂度，遍历一遍数组是n的时间复杂度，总体是O(nlogk)
import heapq
from typing import List, Dict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # 1) 统计频次：O(n)
        count: Dict[int, int] = {}
        for x in nums:
            count[x] = count.get(x, 0) + 1

        # 2) 维护一个大小为 k 的小根堆：堆内存 (freq, val)
        #    这样堆顶永远是“当前堆里频次最小的元素”，方便淘汰
        heap: List[tuple[int, int]] = []
        for val, freq in count.items():
            if len(heap) < k:
                heapq.heappush(heap, (freq, val))  # 先填满 k 个
            else:
                # 如果当前元素频次更大，就替换堆顶（最小频次）
                if freq > heap[0][0]:
                    heapq.heapreplace(heap, (freq, val))

        # 3) 输出堆中的元素值即可（顺序任意）
        return [val for _, val in heap] # 遍历heap中的每个元组，把第一个元素赋值给_（下划线表示这个值不需要用到），第二个元素赋值给val。
