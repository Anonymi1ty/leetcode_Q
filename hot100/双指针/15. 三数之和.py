"""
给你一个整数数组 nums ，判断是否存在三元组 [nums[i], nums[j], nums[k]] 满足 i != j、i != k 且 j != k ，同时还满足 nums[i] + nums[j] + nums[k] == 0 。
请你返回所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组（左右指针指向的数不同）。

示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
解释：
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0 。
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0 。
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0 。
不同的三元组是 [-1,0,1] 和 [-1,-1,2] 。
注意，输出的顺序和三元组的顺序并不重要。
示例 2：

输入：nums = [0,1,1]
输出：[]
解释：唯一可能的三元组和不为 0 。
示例 3：

输入：nums = [0,0,0]
输出：[[0,0,0]]
解释：唯一可能的三元组和为 0 。
"""

# 思路：
    # 先排序，设外层索引 i 从 0 到 n-3 遍历，每次将 nums[i] 作为固定数 a。
    # 再通过双指针法来寻找三元组。
    # 若 a>0，则三数之和最小也大于 0，可直接结束循环。

    # 若 i>0 且 nums[i]==nums[i-1]，跳过，避免重复三元组。

    # 初始化左右指针 l=i+1、r=n-1，目标和为 -a。

    # 当 l<r：
    #  6.1 若 nums[l]+nums[r]==-a，记录 [a,nums[l],nums[r]]；随后移动 l 与 r 跳过相同元素避免重复；
    #  6.2 若和小于 -a，说明需要更大的数，l++；
    #  6.3 若和大于 -a，说明需要更小的数，r--。

    # 返回结果列表 res。
from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Edge case: fewer than 3 numbers
        if len(nums) < 3:
            return []
        
        nums.sort()                       # Step 1: sort the array
        res: List[List[int]] = []
        n = len(nums)

        for i in range(n - 2):            # Step 2: iterate fixed index i
            a = nums[i]
            if a > 0:                     # Step 3: pruning
                break
            if i > 0 and a == nums[i - 1]:# Step 4: skip duplicates for fixed a
                continue

            l, r = i + 1, n - 1           # Step 5: two-pointer setup
            target = -a

            while l < r:                  # Step 6: move pointers
                s = nums[l] + nums[r]
                if s == target:
                    res.append([a, nums[l], nums[r]])
                    # Skip duplicates for nums[l]
                    while l < r and nums[l] == nums[l + 1]:
                        l += 1
                    # Skip duplicates for nums[r]
                    while l < r and nums[r] == nums[r - 1]:
                        r -= 1
                    l += 1
                    r -= 1
                elif s < target:
                    l += 1                # Need a larger sum
                else:
                    r -= 1                # Need a smaller sum
        return res

    