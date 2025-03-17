"""
某套连招动作记作仅由小写字母组成的序列 arr，其中 arr[i] 第 i 个招式的名字。请返回第一个只出现一次的招式名称，如不存在请返回空格。

 

示例 1：

输入：arr = "abbccdeff"
输出：'a'
示例 2：

输入：arr = "ccdd"
输出：' '
"""

# 思路：直接使用哈希表暴力计数，return value == 1的key即可
class Solution:
    def dismantlingAction(self, arr: str) -> str:
        total = {}
        # 统计每个字符的出现次数
        for c in arr:
            # 如果 key 不存在，默认为 0，然后 +1
            total[c] = total.get(c, 0) + 1
        
        # 找到第一个出现一次的字符
        for c in arr:
            if total[c] == 1:
                return c
        
        return ' '  # 没有找到符合条件的字符
            
