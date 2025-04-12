"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

 

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
"""

# 思路：要判断改为:以 −2(...) 结尾的连续子数组的最大和是多少

    # 定义状态（定义子问题）：
        # dp[i]：表示以 nums[i] 结尾 的 连续 子数组的最大和
    # 状态转移方程：
        # 可是 dp[i - 1] 有可能是负数，于是分类讨论：
            # 如果 dp[i - 1] > 0，那么可以把 nums[i] 直接接在 dp[i - 1] 表示的那个数组的后面，得到和更大的连续子数组；
            # 如果 dp[i - 1] <= 0，那么 nums[i] 加上前面的数 dp[i - 1] 以后值不会变大。于是 dp[i] 「另起炉灶」，此时单独的一个 nums[i] 的值，就是 dp[i]。
    # 思考初始值：
        # dp[0] 根据定义，只有 1 个数，一定以 nums[0] 结尾，因此 dp[0] = nums[0]
    # 思考输出：
        # 现在取到了每一个dp[i]的取值，需要存储为list，返回最大值即可

    
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        dp = [float('-inf') for _ in range(size)]
        
        dp[0] = nums[0] # dp[0] 根据定义，只有 1 个数，一定以 nums[0] 结尾
        for i in range(1,size):
            if dp[i - 1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        
        return max(dp)