"""
给定一个整数 n，计算所有小于等于 n 的非负整数中数字 1 出现的个数。

示例 1：

输入：n = 13
输出：6

"""

# 思路：不会，题解也看不懂
    # 高位：当前位左边的数字，记为 high = n // (factor * 10)。
    # 当前位：当前位数字，记为 cur = (n // factor) % 10。
    # 低位：当前位右边的数字，记为 low = n % factor。
class Solution:
    def countDigitOne(self, n: int) -> int:
        digit, res = 1, 0
        high, cur, low = n // 10, n % 10, 0
        while high != 0 or cur != 0:
            if cur == 0: res += high * digit
            elif cur == 1: res += high * digit + low + 1
            else: res += (high + 1) * digit
            low += cur * digit
            cur = high % 10
            high //= 10
            digit *= 10
        return res

            
            
        