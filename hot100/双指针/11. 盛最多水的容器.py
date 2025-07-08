"""
给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

 

示例 1：

输入：[1,8,6,2,5,4,8,3,7]
输出：49 
解释：图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
示例 2：

输入：height = [1,1]
输出：1
"""

# 思路：
    # 判断：在每个状态下，无论长板或短板向中间收窄一格，都会导致水槽 底边宽度 −1​ 变短：
    # 若向内 移动短板 ，水槽的短板 min(h[i],h[j]) 可能变大，因此下个水槽的面积 可能增大 。
    # 若向内 移动长板 ，水槽的短板 min(h[i],h[j])​ 不变或变小，因此下个水槽的面积 一定变小 。
    
        # 使用双指针法
        # 初始化两个指针 left 和 right 分别指向数组的两端
from typing import List

    
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0
        
        while left < right:
            # 计算当前容器的面积
            width = right - left
            current_height = min(height[left], height[right])
            current_area = width * current_height
            
            # 更新最大面积
            max_area = max(max_area, current_area)
            
            # 移动指针
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area