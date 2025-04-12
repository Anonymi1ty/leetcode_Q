"""
请设计一个程序来支持用户在文本编辑器中的模糊搜索功能。用户输入内容中可能使用到如下两种通配符：

'.' 匹配任意单个字符。
'*' 匹配零个或多个前面的那一个元素。
 

请返回用户输入内容 input 所有字符是否可以匹配原文字符串 article。

示例 1：

输入：article = "aa", input = "a"
输出：false
解释："a" 无法匹配 "aa" 整个字符串。
示例 2：

输入：article = "aa", input = "a*"
输出：true
解释：因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
"""

# 思路：不会
    #如果模式串中当前位置的后一个字符是 *（即 j+1 < len(input) 且 input[j+1]=='*'），那么有两种情况：
        # 跳过：忽略“字符+星号”的组合，相当于*匹配零次，即 dp(i, j+2)。
        # 匹配当前字符：如果第一个字符匹配（first_match 为 True），就“消费”掉原字符串的一个字符，继续判断 dp(i+1, j)（这里模式串不动，因为*可以匹配多个前面的字符）。
    
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        memo = {}
    
        def dp(i: int, j: int) -> bool:
            # 如果已经计算过，直接返回保存的结果
            if (i, j) in memo:
                return memo[(i, j)]
            
            # 当模式串遍历完后，只有当原字符串也遍历完才匹配
            if j == len(p):
                return i == len(s)
            
            # 判断当前位置是否匹配（要保证article有字符，并且匹配成功或者模式为'.'）
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')
            
            # 处理'*'字符，注意'*'总是作用于它前面的字符
            if j + 1 < len(p) and p[j + 1] == '*':
                # 两种情况：
                # 1. 跳过当前（pattern[j]和'*'）组合，即dp(i, j+2)
                # 2. 如果当前匹配成功，消耗一个字符，即dp(i+1, j)
                ans = dp(i, j + 2) or (first_match and dp(i + 1, j))
            else:
                # 当前必须匹配成功，然后继续后续匹配
                ans = first_match and dp(i + 1, j + 1)
            
            memo[(i, j)] = ans
            return ans
        return dp(0,0)