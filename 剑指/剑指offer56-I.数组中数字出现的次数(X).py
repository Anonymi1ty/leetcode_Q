"""
整数数组 sockets 记录了一个袜子礼盒的颜色分布情况，其中 sockets[i] 表示该袜子的颜色编号。礼盒中除了一款撞色搭配的袜子，每种颜色的袜子均有两只。

请设计一个程序，在时间复杂度 O(n)，空间复杂度O(1) 内找到这双撞色搭配袜子的两个颜色编号。
"""

# 思路：使用XOR; 并且使用diff_bit = xor_all & -xor_all找到不一样的位数，将他们按这个分为两组

class Solution:
    def sockCollocation(self, sockets: List[int]) -> List[int]:
        # 1. 对数组中所有元素做 XOR，结果为 a ^ b
        xor_all = 0
        for sock in sockets:
            xor_all ^= sock

        # 2. 找到 xor_all 中任意一个为 1 的位（比如右侧第一个为1的位）
        diff_bit = xor_all & -xor_all

        # 3. 根据该位是否为1，将所有元素分为两组，并分别做 XOR
        a, b = 0, 0
        for sock in sockets:
            if sock & diff_bit:
                a ^= sock
            else:
                b ^= sock

        # 此时 a 和 b 就分别是那两个唯一的颜色编号
        return [a, b]
 
        
