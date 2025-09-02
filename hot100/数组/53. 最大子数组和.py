"""
给你一个整数数组 nums ，请你找出一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

子数组是数组中的一个连续部分。

示例 1：

输入：nums = [-2,1,-3,4,-1,2,1,-5,4]
输出：6
解释：连续子数组 [4,-1,2,1] 的和最大，为 6 。
示例 2：

输入：nums = [1]
输出：1
示例 3：

输入：nums = [5,4,-1,7,8]
输出：23
 
"""

# 思路：
    # 当加和为正数时，继续累加，否则就从当前数开始新的累加。
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        # 每个size都先填入负无穷，表示还没有计算过
        dp = [float('-inf') for _ in range(size)]
        
        dp[0] = nums[0] # dp[0] 根据定义，只有 1 个数，一定以 nums[0] 结尾
        for i in range(1,size):
            # 如果前一个 dp[i-1] 大于 0，说明可以继续累加，否则就从 nums[i] 开始
            if dp[i - 1] > 0:
                dp[i] = dp[i-1] + nums[i]
            else:
                dp[i] = nums[i]
        
        return max(dp)