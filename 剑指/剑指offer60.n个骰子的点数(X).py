"""
你选择掷出 num 个色子，请返回所有点数总和的概率。

你需要用一个浮点数数组返回答案，其中第 i 个元素代表这 num 个骰子所能掷出的点数集合中第 i 小的那个的概率。

示例 1：

输入：num = 3
输出：[0.00463,0.01389,0.02778,0.04630,0.06944,0.09722,0.11574,0.12500,0.12500,0.11574,0.09722,0.06944,0.04630,0.02778,0.01389,0.00463]
"""
# https://leetcode.cn/problems/nge-tou-zi-de-dian-shu-lcof/solutions/637778/jian-zhi-offer-60-n-ge-tou-zi-de-dian-sh-z36d/
# 思路：要判断改为:从 num(最小值) 到 6^num(最大值)，分别的概率
    # 假设已知 n−1 个骰子的解 f(n−1) ，此时添加一枚骰子，求 n 个骰子的点数和为 x 的概率 f(n,x) 。
    # 当添加骰子的点数为 1 时，前 n−1 个骰子的点数和应为 x−1 ，方可组成点数和 x ；同理，当此骰子为 2 时，前 n−1 个骰子应为 x−2 ；
        # 以此类推，直至此骰子点数为 6 。将这 6 种情况的概率相加，即可得到概率 f(n,x) 

    
    # 定义状态（定义子问题）：
        # 使用二维数组 dp，其中 dp[i][j] 表示用 i 个骰子得到和为 j 的组合数。
    # 状态转移方程：
        # 当已经有 i-1 个骰子的结果时，添加第 i 个骰子：
        # 如果第 i 个骰子点数为 k，那么前 i-1 个骰子的和必须为 j-k；
        # 对每一个 k (1~6) 累加 dp[i-1][j-k] 得到 dp[i][j]。
    # 思考初始值：
        # 当只有1个骰子时，出现点数 1 到 6 的组合数都是1。
    # 思考输出：
        # return res

    
class Solution:
    def statisticsProbability(self, num: int) -> List[float]:
        # 定义 dp 数组：
        # dp[i][j] 表示投 i 个骰子获得和为 j 的方案数。
        # 投 i 个骰子最小的和为 i，最大的和为 6*i，所以 dp 的 j 需要覆盖 0 到 6*num（部分位置不会用到）。
        dp = [[0] * (6 * num + 1) for _ in range(num + 1)]
        
        # 初始化：只有一个骰子时，出现点数 1 到 6 的方案数均为 1
        for face in range(1, 7):
            dp[1][face] = 1
        
        # 状态转移：
        # 对于 i 个骰子，当添加第 i 个骰子时，
        # 如果第 i 个骰子的结果为 k (1 ≤ k ≤ 6)，
        # 则前 i−1 个骰子的和必须为 j − k，
        # 故状态转移方程为：
        # dp[i][j] += dp[i-1][j-k]
        for dice in range(2, num + 1):
            # 合法的和从 dice 到 6*dice
            for j in range(dice, 6 * dice + 1):
                for k in range(1, 7):
                    # 保证 j - k 在 i-1 个骰子的可能和的范围内：最小为 dice-1，最大为 6*(dice-1)
                    if dice - 1 <= j - k <= 6 * (dice - 1):
                        dp[dice][j] += dp[dice - 1][j - k]
        
        # 总结果数为 6^num，因为每个骰子有6种可能。
        total = 6 ** num
        
        # 根据 dp[num] 中从 num 到 6*num 的结果计算概率，
        # 并按照从最小和到最大和的顺序存入 result 数组中。
        result = []
        for s in range(num, 6 * num + 1):
            # 计算概率并保留5位小数（如示例所示）
            probability = dp[num][s] / total
            result.append(round(probability, 5))
        
        return result