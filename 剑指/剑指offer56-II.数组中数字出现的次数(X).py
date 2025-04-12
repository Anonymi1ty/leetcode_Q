"""
教学过程中，教练示范一次，学员跟做三次。该过程被混乱剪辑后，记录于数组 actions，其中 actions[i] 表示做出该动作的人员编号。请返回教练的编号。
示例 1：

输入：actions = [5, 7, 5, 5]
输出：7
示例 2：

输入：actions = [12, 1, 6, 12, 6, 12, 6]
输出：1
"""

# 思路：使用XOR; 我们用两个变量来记录每一位的出现状态：（00-->01-->10-->00...）
    # ones：记录当前哪些位出现次数模 3 后为 1（也就是当前只出现过一次的位）。
    # twos：记录当前哪些位出现次数模 3 后为 2（也就是当前出现过两次的位）。

class Solution:
    def trainingPlan(self, actions: List[int]) -> int:
        ones, twos = 0, 0
        for action in actions:
            ones = ones ^ action & ~twos
            twos = twos ^ action & ~ones
        return ones
        
