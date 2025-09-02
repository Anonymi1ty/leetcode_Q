"""
给你一个整数数组 nums 和一个整数 k ，请你统计并返回 该数组中和为 k 的子数组的个数 。

子数组是数组中元素的连续非空序列。


示例 1：

输入：nums = [1,1,1], k = 2
输出：2
示例 2：

输入：nums = [1,2,3], k = 3
输出：2
"""

# 思路：
    # 初始化 count=0、prefix=0，并用哈希表 freq{0:1} 存“前缀和 = 0”出现 1 次；

    # 依次遍历 nums：每到元素 x 更新 prefix += x；

    # 设目标差值 need = prefix - k；若 need 已在 freq 中，则说明此前出现过若干前缀和为 need 的位置，每出现一次就对应一个子数组和为 k，于是 count += freq[need]；

    # 将当前 prefix 写入 freq[prefix] += 1；

    # 遍历结束返回 count；

    # 整体时间复杂度 O(n)，空间 O(n)（最坏情况下所有前缀和互不相同）；

    # 该方法对负数、零以及任意 k 都通用
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1          # 空前缀
        pre = 0
        count = 0

        for x in nums:
            pre += x
            count += freq[pre - k]   # 步骤 3
            freq[pre] += 1           # 步骤 4
        return count
