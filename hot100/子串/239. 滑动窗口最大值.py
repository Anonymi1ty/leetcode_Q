"""
给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。

返回 滑动窗口中的最大值 。

 

示例 1：

输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
输出：[3,3,5,5,6,7]
解释：
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7
示例 2：

输入：nums = [1], k = 1
输出：[1]
"""

# 思路（大根堆）：
    # 维护一个最大堆保存当前窗口候选元素；Python 只有小根堆，所以把数值取负存成 (-nums[i], i)。

    # 堆顶永远是当前最大值的候选，但可能过期（索引落在窗口左边）。

    # 每次右移窗口：

    # 把新元素 (−nums[i], i) 推入堆；

    # 反复弹出堆顶，直到堆顶的索引 idx > i-k，确保它落在当前窗口 [i-k+1, i] 内；

    # 此时堆顶即为当前窗口最大值。

    # 这种“不过期不清，取用时再丢”的做法叫 懒删除，能避免在堆中做中间元素删除的额外开销。
import heapq
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        if n == 0 or k == 0:
            return []
        if k == 1:
            return nums[:]  # 每个窗口就一个元素

        # 1) 初始化：把前 k 个元素入堆（用 -value 模拟最大堆）
        #   堆元素：(-value, index)
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)

        ans = []
        # 2) 先记录第一个窗口的最大值
        ans.append(-heap[0][0]) # 堆顶的index=0的存储，即−nums[i]

        # 3) 从第 k 个元素开始滑动窗口到右端
        for i in range(k, n):
            # 3.1 推入新元素
            heapq.heappush(heap, (-nums[i], i))

            # 3.2 懒删除：把堆顶中过期元素（索引 <= i - k）弹出
            #     当前窗口为 [i-k+1, i]，索引必须 > i-k 才是有效的
            while heap and heap[0][1] <= i - k: # # 堆顶的index=1的存储，即i
                heapq.heappop(heap)

            # 3.3 此时堆顶即为当前窗口最大值
            ans.append(-heap[0][0])

        return ans