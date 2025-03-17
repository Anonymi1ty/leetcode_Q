"""（奇怪的题，纯规则运算）
有效数字（按顺序）可以分成以下几个部分：

若干空格
一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
若干空格
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

 

示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
 

提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，空格 ' ' 或者点 '.' 。
"""

# 思路：拆分规则，逐一验证
    # 1.去除前后空格
         # 允许数字前后存在空格，去除前后空格后再进行处理。
         
    # 2.拆分科学计数法的 e 或 E
        # 科学计数法中 e 或 E 将数字拆分为底数和指数两个部分。
        # e 或 E 必须要有前后部分，不能单独存在，例如 "e3" 是无效的。
        
    # 3.验证底数（小数或整数）
        # 允许带 + 或 - 号。
        # 可以是小数或整数：
            # 小数格式:
            # 至少一位数字后面跟着 .（如 "4."）。
            # . 后面至少一位数字（如 ".5"）。
            # 至少一位数字 . 后面再接至少一位数字（如 "3.14"）。
        # 整数格式:
            # 只能是 [+-]?[0-9]+ 形式。
            
    # 验证指数部分（整数）
        # 只能是整数，不能带 .
        # 允许 + 或 - 号，但不能只有符号（如 "3e+" 无效）
        # 不能是空字符串（如 "3e" 无效）


class Solution:
    def validNumber(self, s: str) -> bool:
        # 去除前后空格
        s = s.strip()
        
        # 检查是否有 'e' 或 'E'，并拆分底数和指数
        if 'e' in s or 'E' in s:
            parts = s.split('e') if 'e' in s else s.split('E')
            if len(parts) != 2:  # 'e' 或 'E' 不能单独出现，且只能有一个
                return False
            base, exponent = parts
            return self.isDecimalOrInteger(base) and self.isInteger(exponent)
        
        # 如果没有 'e'，只需检查是否是整数或小数
        return self.isDecimalOrInteger(s)
    
    def isDecimalOrInteger(self, s: str) -> bool:
        """ 检查是否是有效的整数或小数 """
        if not s:
            return False
        
        if s[0] in "+-":
            s = s[1:]  # 去掉正负号
        
        if not s:
            return False  # 不能只剩下 `+` 或 `-`
        
        if '.' in s:
            parts = s.split('.')
            if len(parts) != 2:  # 只能有一个 `.`
                return False
            left, right = parts
        # 必须保证 `left` 和 `right` **都是空或数字**
            if (left and not left.isdigit()) or (right and not right.isdigit()):
                return False
            # 至少一部分要有数字（左侧或右侧），if left else False 的意思是如果 left 为空，就不检查了
            return (left.isdigit() if left else False) or (right.isdigit() if right else False)
        
        # 纯整数情况
        return s.isdigit()
    
    def isInteger(self, s: str) -> bool:
        """ 检查是否是有效整数（用于指数部分） """
        if not s:
            return False

        if s[0] in "+-":
            s = s[1:]  # 去掉正负号
        
        return s.isdigit()  # 指数部分只能是整数

        