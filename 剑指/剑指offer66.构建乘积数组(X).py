"""
为了深入了解这些生物群体的生态特征，你们进行了大量的实地观察和数据采集。数组 arrayA 记录了各个生物群体数量数据，其中 arrayA[i] 表示第 i 个生物群体的数量。
请返回一个数组 arrayB，该数组为基于数组 arrayA 中的数据计算得出的结果，其中 arrayB[i] 表示将第 i 个生物群体的数量从总体中排除后的其他数量的乘积。

 

示例 1：

输入：arrayA = [2, 4, 6, 8, 10]
输出：[1920, 960, 640, 480, 384]
 

提示：

所有元素乘积之和不会溢出 32 位整数
arrayA.length <= 100000
"""

# 思路：首先不能用除法，因为测试用例里面有0。
    # 可以理解成对角线全为1的矩阵，总乘机=其左边所有元素的乘积 * 其右边所有元素的乘积（两次循环遍历）

class Solution:
    def statisticalResult(self, arrayA: List[int]) -> List[int]:
        n = len(arrayA)
        res = [1] * n
        # 计算左边的乘积
        for i in range(1, n):
            res[i] = res[i-1] * arrayA[i-1]
        tmp = 1
        # n-2的意思是最后一行不用计算右三角，"-1":循环会在 i 达到 -1 之前停止运行，"-1":是每次减1
        for i in range(n-2, -1, -1):
            tmp *= arrayA[i+1]
            res[i] *= tmp
        return res
        