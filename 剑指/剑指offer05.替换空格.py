# 题目：
"""
假定一段路径记作字符串 path，其中以 "." 作为分隔符。现需将路径加密，加密方法为将 path 中的分隔符替换为空格 " "，请返回加密后的字符串。
示例 1：

输入：path = "a.aef.qerf.bb"

输出："a aef qerf bb"
"""

# 正常思路：for循环，遍历字符串，遇到"."替换成空格。最后返回" ".join(res)即可
class Solution:
    def pathEncryption(self, path: str) -> str:
        res = path.replace(".", " ")
        return res