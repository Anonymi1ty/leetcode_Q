"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：

输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
"""

# 思路：
    # 图解：https://leetcode.cn/problems/trapping-rain-water/solutions/186762/wei-en-tu-jie-fa-zui-jian-dan-yi-dong-10xing-jie-j/?envType=study-plan-v2&envId=top-100-liked
    # 从左往右遍历得S1，每步S1+=max1且max1逐步增大(柱子)
    # 同样地，从右往左遍历可得S2。
    # 于是我们有如下发现，S1 + S2会覆盖整个矩形，并且：重复面积 = 柱子面积 + 积水面积
    # 最终， 积水面积 = S1 + S2 - 矩形面积 - 柱子面积
from typing import List

    
class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        s1, s2 = 0, 0
        max1, max2 = 0, 0
         
        for i in range(n):
            if max1 < height[i]: # 从左往右
                max1 = height[i]
            if max2 < height[n - i -1]: # 从右往左
                max2 = height[n - i -1]
            s1 += max1
            s2 += max2
        res = s1 + s2 - max1 * len(height) - sum(height)
        return res