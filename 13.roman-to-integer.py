#
# @lc app=leetcode id=13 lang=python3
#
# [13] Roman to Integer
#

# @lc code=start
class Solution:
    def romanToInt(self, s: str) -> int:
        # 定义字符
        dic = {}
        dic["I"] = 1
        dic["IV"] = 4
        dic["V"] = 5
        dic["IX"] = 9
        dic["X"] = 10
        dic["XL"] = 40
        dic["L"] = 50
        dic["XC"] = 90
        dic["C"] = 100
        dic["CD"] = 400
        dic["D"] = 500
        dic["CM"] = 900
        dic["M"] = 1000
        # 接下来对str判断，遍历时检查下一个值
        i = 0
        res = 0
        # i是下标
        while i < len(s):
            # 如果i+1小于s的长度，并且s[i:i+2]在dic中 [i,i+2)是左闭右开区间
            if i + 1 < len(s) and s[i:i+2] in dic:
                res += dic[s[i:i+2]]
                i += 2
            else:
                res += dic[s[i]]
                i += 1
        return res
        
        
# @lc code=end

