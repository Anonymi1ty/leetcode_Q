"""
实现 pow(x, n) ，即计算 x 的整数 n 次幂函数（即，x^n ）。

示例 1：

输入：x = 2.00000, n = 10
输出：1024.00000
"""

# 思路：不能使用简单循环，会超时；所以使用快速幂：
    # 根据推导，可通过循环 x=x^2  操作，每次把幂从 n 降至 n//2 ，直至将幂降为 0

class Solution:
    def myPow(self, x: float, n: int) -> float:
        # 处理负数指数
        if n < 0:
            x = 1 / x
            n = -n
        
        res = 1.0
        # 快速幂的迭代实现
        while n > 0:
            # 如果当前 n 为奇数，则乘上当前的 x
            if n % 2 == 1:
                res *= x
            # 每次翻倍 x(x = x^2)
            x *= x
            # 相当于 n //= 2
            n //= 2
        return res


            
            
        