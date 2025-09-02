"""
给定一个整数数组 nums，将数组中的元素向右轮转 k 个位置，其中 k 是非负数。

 

示例 1:

输入: nums = [1,2,3,4,5,6,7], k = 3
输出: [5,6,7,1,2,3,4]
解释:
向右轮转 1 步: [7,1,2,3,4,5,6]
向右轮转 2 步: [6,7,1,2,3,4,5]
向右轮转 3 步: [5,6,7,1,2,3,4]
示例 2:

输入：nums = [-1,-100,3,99], k = 2
输出：[3,99,-1,-100]
解释: 
向右轮转 1 步: [99,-1,-100,3]
向右轮转 2 步: [3,99,-1,-100]
"""

# 思路：
    # 切片后合并
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # list_1是左边变的长度，是len(nums) - k % len(nums)，取模是因为害怕k大于nums的长度，导致切片越界
        list_1 = nums[:len(nums) - k % len(nums)]
        # list_2是右边变的长度，是k % len(nums)
        list_2 = nums[len(nums) - k % len(nums):]
        # nums[:]是nums的切片，[:]表示修改原数组
        nums[:] = list_2 + list_1
        
        