"""
给定两个字符串 s 和 p，找到 s 中所有 p 的 异位词 的子串，返回这些子串的起始索引。不考虑答案输出的顺序。

示例 1:

输入: s = "cbaebabacd", p = "abc"
输出: [0,6]
解释:
起始索引等于 0 的子串是 "cba", 它是 "abc" 的异位词。
起始索引等于 6 的子串是 "bac", 它是 "abc" 的异位词。
 示例 2:

输入: s = "abab", p = "ab"
输出: [0,1,2]
解释:
起始索引等于 0 的子串是 "ab", 它是 "ab" 的异位词。
起始索引等于 1 的子串是 "ba", 它是 "ab" 的异位词。
起始索引等于 2 的子串是 "ab", 它是 "ab" 的异位词。
"""

# 思路：
    # 使用双指针和滑动窗口的方式遍历字符串 s，检查当前窗口的排序后的字符是否和p相同
from typing import List
from collections import deque
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # # 将p的字符频率存储在字典中
        # p_count = {}
        # for char in p:
        #     p_count[char] = p_count.get(char, 0) + 1
        res = []
        s_count = deque()  # 用于存储当前窗口的字符
        p_length = len(p)
        left = 0
        sorted_p = sorted(p)
        for right in range(len(s)):
            # 将当前字符加入窗口
            s_count.append(s[right])
            # 如果窗口大小超过p的长度，移除左边的字符
            if len(s_count) > p_length:
                s_count.popleft()
                left += 1
            
            # 检查当前窗口是否是p的异位词
            if len(s_count) == p_length and sorted(s_count) == sorted_p:
                res.append(left)
        return res
        