"""
给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用 0 来代替。

 

示例 1:

输入: temperatures = [73,74,75,71,69,72,76,73]
输出: [1,1,4,2,1,1,0,0]
示例 2:

输入: temperatures = [30,40,50,60]
输出: [1,1,1,0]
示例 3:

输入: temperatures = [30,60,90]
输出: [1,1,0]

"""

# 思路：
    # 所有的温度都以[坐标]入栈
    # 保证入栈的元素都以递减顺序排列（栈底元素大），否则计算坐标差值作为结果，之后出栈
    # 如果遍历结束，站内的元素都填入0作为结果
    
    

from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        ans = [0] * n                 # 结果数组，默认 0
        stack = []                    # 单调递减栈：存“下标”，满足 temperatures[stack[i]] 递减

        for i, t in enumerate(temperatures):
            # 当前温度一旦高于栈顶下标对应的温度，就可以为栈顶下标结算答案
            while stack and t > temperatures[stack[-1]]:
                j = stack.pop()       # j 是更低温的那一天
                ans[j] = i - j        # 从 j 到 i 的间隔天数
            stack.append(i)           # 当前下标入栈，等待将来更高温来结算

        return ans
