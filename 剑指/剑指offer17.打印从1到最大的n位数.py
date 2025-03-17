"""
实现一个十进制数字报数程序，请按照数字从小到大的顺序返回一个整数数列，该数列从数字 1 开始，到最大的正整数 cnt 位数字结束。
"""

from typing import List


class Solution:
    def countNumbers(self, cnt: int) -> List[int]:
        res = []
        i = 1
        while i <= (10**cnt)-1:
            res.append(i)
            i += 1
        return res