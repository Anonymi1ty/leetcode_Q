"""
给你一个整数 n ，请你找出并返回第 n 个 丑数 。

丑数 就是质因子只包含 2、3 和 5 的正整数。

 

示例 1：

输入：n = 10
输出：12
解释：[1, 2, 3, 4, 5, 6, 8, 9, 10, 12] 是由前 10 个丑数组成的序列。

示例 2：

输入：n = 1
输出：1
解释：1 通常被视为丑数。
"""

# 核心思想：丑数都是以其它较小的丑数*2/3/5得到的，按照顺序排序返回第n个即可
    # 顺序统计丑数列表：三个指针分别指向2,3,5每一步都求min即可

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        # 生成n个全为1的数组（因为1是特殊的丑数）
        res = [1] * n
        # abc都指向第一个位置
        a,b,c = 0,0,0
        for i in range(1,n):
            # 定义*2/3/5
            times_2, times_3, times_5 = res[a]*2, res[b]*3, res[c]*5
            # 选最小的加入res（相当于排序）
            res[i] = min(times_2, times_3, times_5)
            # 如果使用了一个数字，指针向右移动一位
            if res[i] == times_2:
                a += 1
            if res[i] == times_3:
                b += 1
            if res[i] == times_5:
                c += 1
        # 返回最后一个加入的数
        return res[-1]