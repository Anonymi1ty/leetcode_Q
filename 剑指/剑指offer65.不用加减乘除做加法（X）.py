"""
计算机安全专家正在开发一款高度安全的加密通信软件，需要在进行数据传输时对数据进行加密和解密操作。假定 dataA 和 dataB 分别为随机抽样的两次通信的数据量：

正数为发送量
负数为接受量
0 为数据遗失
请不使用四则运算符的情况下实现一个函数计算两次通信的数据量之和（三种情况均需被统计），以确保在数据传输过程中的高安全性和保密性。

 

示例 1：

输入：dataA = 5, dataB = -1
输出：4
"""

# 思路：使用位运算来实现加法。我们可以使用异或运算来计算不考虑进位的和，然后使用与运算和左移来计算进位，直到没有进位为止。
    # Python 中整数的位数是无限的，但对于位运算实现加法时，通常需要模拟固定宽度（如 32 位）的情况。

class Solution:
    def encryptionCalculate(self, dataA: int, dataB: int) -> int:
        # 定义 32 位整数的最大正数和掩码
        MAX = 0x7FFFFFFF
        mask = 0xFFFFFFFF
        
        a = dataA
        b = dataB
        
        # 迭代，直到没有进位
        while b != 0:
            # 无进位和（使用异或运算）并应用掩码
            sum_without_carry = (a ^ b) & mask #我们可以用 a ^ b 得到所有不考虑进位的和。注意：我们需要将其应用掩码，以确保结果在 32 位范围内。
            # 计算进位（使用与运算并左移一位）并应用掩码
            carry = ((a & b) << 1) & mask #我们可以用 a & b 得到所有进位的位置。但注意：进位应当加到相邻的高一位，所以需要将其左移一位，即 (a & b) << 1。
            a, b = sum_without_carry, carry
        
        # 如果结果在正数范围内直接返回，否则进行补码转换得到负数
        return a if a <= MAX else ~(a ^ mask)

        
        
