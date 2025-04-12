"""
斐波那契数 （通常用 F(n) 表示）形成的序列称为 斐波那契数列 。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0，F(1) = 1
F(n) = F(n - 1) + F(n - 2)，其中 n > 1
给定 n ，请计算 F(n) 。

答案需要取模 1e9+7(1000000007) ，如计算初始结果为：1000000008，请返回 1。
"""

# 思路：递归会超时，动态规划

# class Solution:
#     def fib(self, n: int) -> int:
#         if n == 0:
#             return 0
#         if n == 1:
#             return 1
#         return self.fib(n-1) + self.fib(n-2)
        
class Solution:
    def fib(self, n: int) -> int:
        MOD = 1000000007  # 模数
        if n < 2:
            return n
        a, b = 0, 1  # 初始化 F(0) 和 F(1)
        # 从 2 开始迭代，直到 n
        for _ in range(2, n + 1):
            a, b = b, (a + b) % MOD
        return b