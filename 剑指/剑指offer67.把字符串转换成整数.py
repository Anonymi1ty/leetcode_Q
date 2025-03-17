"""
书店店员有一张链表形式的书单，每个节点代表一本书，节点中的值表示书的编号。
为更方便整理书架，店员需要将书单倒过来排列，就可以从最后一本书开始整理，逐一将书放回到书架上。请倒序返回这个书单链表。

 
示例 1：

输入：head = [3,6,4,1]

输出：[1,4,6,3]

"""

# 思路：

class Solution:
    def myAtoi(self, s: str) -> int:
        # 1. 去除前后空格
        s = s.strip()
        if not s:  # 处理空字符串情况
            return 0

        # 2. 处理正负号
        type_sign = 1  # 默认是正数
        index = 0
        if s[0] == "-":
            type_sign = -1
            index += 1
        elif s[0] == "+":
            index += 1

        # 3. 读取数字部分
        res_s = ""
        while index < len(s) and s[index].isdigit():
            res_s += s[index]
            index += 1
        
        if not res_s:  # 处理字符串没有数字的情况
            return 0
        
        # 4. 转换成整数，并截断超出范围的情况
        res = int(res_s) * type_sign
        int_min, int_max = -2**31, 2**31 - 1
        if res < int_min:
            return int_min
        if res > int_max:
            return int_max
        return res

            
