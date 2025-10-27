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

# 思路（前缀和 + 哈希表）：
# -----------------------------------------------------
# 1️⃣ 定义前缀和 prefix[i] 表示从 nums[0] 到 nums[i] 的元素之和。
#     若存在两个下标 i < j，使得 prefix[j] - prefix[i] == k，
#     则说明区间 (i, j] 内的子数组和为 k。
#
# 2️⃣ 我们用哈希表 freq 来统计“某个前缀和出现的次数”。
#     初始 freq[0] = 1，表示空前缀的和为 0（方便处理从起点开始的子数组）。
#
# 3️⃣ 遍历数组元素 x，不断更新当前前缀和 prefix。
#     若在哈希表中存在 prefix - k，说明此前某一位置的前缀和为 (prefix - k)，
#     从那之后到当前位置的子数组之和正好为 k。
#     因此计数器 count += freq[prefix - k]。
#
# 4️⃣ 最后别忘了更新当前前缀和在哈希表中的次数：freq[prefix] += 1。
#
# 5️⃣ 遍历结束，count 即为所有满足条件的子数组个数。
from typing import List
from collections import defaultdict

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1          # 初始空前缀，和为0出现一次
        prefix = 0           # 当前前缀和
        count = 0            # 统计子数组数量

        # 遍历数组
        for x in nums:
            prefix += x       # 更新当前前缀和
            # 若存在某前缀和为 (prefix - k)，则对应一个和为 k 的子数组
            count += freq[prefix - k] # prefix比k大了多少，检查前缀有没有这个数；有的话说明截断这个前缀和大小刚好为k
            # 记录当前前缀和出现次数（为后续子数组提供匹配）
            freq[prefix] += 1

        return count