"""
现有一串神秘的密文 ciphertext，经调查，密文的特点和规则如下：

密文由非负整数组成
数字 0-25 分别对应字母 a-z
请根据上述规则将密文 ciphertext 解密为字母，并返回共有多少种解密结果。

示例 1：

输入：ciphertext = 216612
输出：6
解释：216612 解密后有 6 种不同的形式，分别是 "cbggbc"，"vggbc"，"vggm"，"cbggm"，"cqgbc" 和 "cqgm" 
"""

# 思路：字符串为x1 x2 ...xi 要判断改为:以 xi 为结尾的数字的翻译方案数量

    # 定义状态（定义子问题）：
        # 设动态规划列表 dp ，dp[i] 代表以 xi 为结尾的数字的翻译方案数量
    # 状态转移方程：
        # 若 xi 和 xi−1  组成的两位数字可被整体翻译，则 dp[i]=dp[i−1]+dp[i−2] ，否则 dp[i]=dp[i−1] 。
    # 思考初始值：
        # 初始状态： dp[0]=dp[1]=1 ，即 “无数字” 和 “第 1 位数字” 的翻译方法数量均为 1 ；(dp[0] = 1是因为 dp[2] = 2 如果符合条件，所以才得出)
    # 思考输出：
        # dp[n] ，即此数字的翻译方案数量；

    
class Solution:
    def crackNumber(self, ciphertext: int) -> int:
        # 将数字转换为字符串，便于逐位操作
        s_ciphertext = str(ciphertext)
        size = len(s_ciphertext)
        
        # 如果字符串为空，直接返回 0 解法（根据题目，这种情况一般不出现）
        if size == 0:
            return 0
        
        # dp 数组长度为 size+1，其中 dp[i] 表示前 i 位的翻译方案数
        dp = [0] * (size + 1)
        dp[0] = 1       # 空字符串视为有 1 种翻译方法
        dp[1] = 1       # 第一位数字必定有 1 种翻译方式
        
        # 遍历从第二位数字开始，i 表示前 i 个字符构成的子串
        for i in range(2, size + 1):
            
            # 拼接第 i-2 和 i-1 个字符构成两位数
            two_digit = int(s_ciphertext[i-2:i])
            # 如果两位数在合法范围内（10到25），可以合并翻译
            if 10 <= two_digit <= 25:
                dp[i] = dp[i-2] + dp[i-1]
            else:
                # 单独翻译第 i-1 个字符
                dp[i] = dp[i-1]
        
        return dp[size]