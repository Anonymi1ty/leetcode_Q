"""
现有一个记作二维矩阵 frame 的珠宝架，其中 frame[i][j] 为该位置珠宝的价值。拿取珠宝的规则为：

只能从架子的左上角开始拿珠宝
每次可以移动到右侧或下侧的相邻位置
到达珠宝架子的右下角时，停止拿取
注意：珠宝的价值都是大于 0 的。除非这个架子上没有任何珠宝，比如 frame = [[0]]。

 

示例 1：

输入：frame = [[1,3,1],[1,5,1],[4,2,1]]
输出：12
解释：路径 1→3→5→2→1 可以拿到最高价值的珠宝
"""

# 思路：要判断改为:以 frame[i][j] 结尾的连续子数组的最大和是多少;且dp[i][j] = dp[i-1][j] + frame[i][j] or dp[i][j] = dp[i][j - 1] + frame[i][j]

    # 定义状态（定义子问题）：
        # dp[i][j]：表示以 frame[i][j] 结尾 的路径的最大和
    # 状态转移方程：
        # 总结可以写成 dp[i][j] = max(dp[i-1][j] + frame[i][j] , dp[i][j - 1] + frame[i][j])
    # 思考初始值：
        # dp[0][0] 根据定义，只能从左上角开始，因此 dp[0][0] = frame[0][0]
    # 思考输出：
        # return dp[m -1, n - 1]

    
class Solution:
    def jewelleryValue(self, frame: List[List[int]]) -> int:
         # 计算矩阵的行数和列数
        n = len(frame)        # 行数
        m = len(frame[0])     # 列数
        
        # dp[i][j] 表示从左上角 (0,0) 到 (i, j) 的最大珠宝价值
        dp = [[0] * m for _ in range(n)]
        
        # 初始状态：起始点的价值就是自身的珠宝价值
        dp[0][0] = frame[0][0]
        
        # 初始化第一行：只能从左侧走来
        for j in range(1, m):
            dp[0][j] = dp[0][j-1] + frame[0][j]
            # 注：第一行的路径只能由前面的格子累加而来
        
        # 初始化第一列：只能从上面走来
        for i in range(1, n):
            dp[i][0] = dp[i-1][0] + frame[i][0]
            # 注：第一列的路径只能由上面的格子累加而来
            
        # 计算其余位置的状态，每个位置可以由上边或左边到达，取较大值
        for i in range(1, n):
            for j in range(1, m):
                dp[i][j] = max(dp[i-1][j], dp[i][j-1]) + frame[i][j]
                # 注释：选择上方或左侧中的较大者加上当前位置的价值
        
        # 返回右下角的最大珠宝价值
        return dp[n-1][m-1]