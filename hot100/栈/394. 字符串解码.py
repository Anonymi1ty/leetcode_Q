"""
给定一个经过编码的字符串，返回它解码后的字符串。

编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。注意 k 保证为正整数。

你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。

此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

测试用例保证输出的长度不会超过 105。

 

示例 1：

输入：s = "3[a]2[bc]"
输出："aaabcbc"
"""
# 思路：线性扫描字符串，遇到数字累计倍数 k，遇到 [ 把当前已构造的字符串与 k 入栈，遇到 ] 弹栈并拼接重复段；字母则直接追加到当前字符串。

from collections import deque

class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = deque()   # 存放重复次数 k
        str_stack = deque()   # 存放进入方括号前的“已完成字符串”
        curr_num = 0          # 当前解析到的数字 k
        curr_str = []         # 当前层正在构造的字符串（用list拼接更高效）

        for ch in s:
            if ch.isdigit():
                # 累计多位数，如"12[...]" -> 12
                curr_num = curr_num * 10 + (ord(ch) - ord('0'))
            elif ch == '[':
                # 进入新的一层：把当前层的结果与倍数压栈，重置
                num_stack.append(curr_num)
                str_stack.append(''.join(curr_str))
                curr_num = 0
                curr_str = []
            elif ch == ']':
                # 结束当前层：弹出倍数与前缀，拼接重复段
                k = num_stack.pop()
                prev = str_stack.pop()
                curr_str = [prev + ''.join(curr_str) * k]
            else:
                # 普通字母，直接加入当前层
                curr_str.append(ch)

        return ''.join(curr_str)
