"""
给定一个正整数 n，编写一个函数，获取一个正整数的二进制形式并返回其二进制表达式中 设置位 的个数（也被称为汉明重量）。

示例 1：

输入：n = 11
输出：3
解释：输入的二进制串 1011 中，共有 3 个设置位。
"""

# 思路：使用python中的现成函数format/bin

class Solution:
    def hammingWeight(self, n: int) -> int:
        bi_num = format(n, 'b')
        res = bi_num.count('1')
        return res

            
            
        