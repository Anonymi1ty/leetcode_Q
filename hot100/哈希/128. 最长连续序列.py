"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
示例 3：

输入：nums = [1,0,1,2]
输出：3
"""

# 思路：
    # 要求在 O(n) 时间复杂度内解决，因此不能排序，应该使用 哈希集合（Set） 来实现快速查找
        #遍历数组，对于每个数 num：
            # 如果 num - 1 不在集合中，说明 num 是某个序列的起点；
            # 从 num 向后找连续的数字 num + 1, num + 2, ...；
            # 统计该序列的长度，更新最长长度。

    
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 将全部的nums存储在hashset中
        num_set = set(nums)
        max_len = 0
        
        for num in num_set:
            if num - 1 not in num_set:
                current = num 
                length = 1
                while current + 1 in num_set:
                    current += 1
                    length += 1
                max_len = max(length, max_len)
        
        return max_len