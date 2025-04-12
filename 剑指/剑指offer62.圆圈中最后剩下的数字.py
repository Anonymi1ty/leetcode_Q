"""
社团共有 num 位成员参与破冰游戏，编号为 0 ~ num-1。成员们按照编号顺序围绕圆桌而坐。
社长抽取一个数字 target，从 0 号成员起开始计数，排在第 target 位的成员离开圆桌，且成员离开后从下一个成员开始计数。请返回游戏结束时最后一位成员的编号。

示例 1：

输入：num = 7, target = 4
输出：1
示例 2：

输入：num = 12, target = 5
输出：0
"""

# 思路：

    # 定义状态（定义子问题）：
        # 设动态规划列表 dp ，dp[i] 代表 i 个人， target是 m 时，的题解
    # 状态转移方程：
        # dp[i]=[dp[i-1] + m] % i。(模拟删除)
    # 思考初始值：
        # 初始状态： 1,m 问题」的解恒为 0 ，即 dp[0]=0
    # 思考输出：
        # dp[n] 

    
class Solution:
    def iceBreakingGame(self, num: int, target: int) -> int:
        dp = [ 0 for _ in range(num)]
        
        dp[0] = 0
        for i in range(1,num):
            dp[i] = (dp[i-1] + target) % (i + 1)
        
        return dp[num - 1]