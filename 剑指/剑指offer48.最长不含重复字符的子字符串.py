"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长 子串 的长度。

 

示例 1:

输入: s = "abcabcbb"
输出: 3 
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。
示例 2:

输入: s = "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。
示例 3:

输入: s = "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""

# 思路：滑动窗口，如果遇到不一样的len+1,visited右侧入栈,右指针向右;
    # 如果遇到一样的len -= 1, 左边窗口向右移动一个，visited左侧出栈，检测是否还有一样的，有一样的重复上述操作，直到不重复或者left == right；
    # 如果left == right 从头重复上述操作，直到right =len(s)
        # visited最好是双端队列,res = []最后返回最大值
from collections import deque

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0  # 左指针
        right = 0  # 右指针
        visited = deque()  # 记录当前窗口中的字符
        max_len = 0  # 记录最大无重复子串的长度
        
        while right < len(s):
            if s[right] not in visited:
                # 遇到新字符，加入窗口，更新最大长度
                visited.append(s[right])
                max_len = max(max_len, len(visited))
                right += 1
            else:
                # 遇到重复字符，从左边依次移除，直到去掉重复字符
                while s[right] in visited:
                    visited.popleft()
                    left += 1
                # 处理完重复字符后，把当前字符加入窗口
                visited.append(s[right])
                right += 1

        return max_len
