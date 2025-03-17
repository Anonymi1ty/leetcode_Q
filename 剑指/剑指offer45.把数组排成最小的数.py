"""
闯关游戏需要破解一组密码，闯关组给出的有关密码的线索是：

一个拥有密码所有元素的非负整数数组 password
密码是 password 中所有元素拼接后得到的最小的一个数
请编写一个程序返回这个密码。
 

示例 1：

输入：password = [15, 8, 7]
输出："1578"
示例 2：

输入：password = [0, 3, 30, 34, 5, 9]
输出："03033459"
"""

# 可以理解成数组进行两个对比，当 x "拼接" y < y "拼接" x时,证明x应该在y的左侧，每组进行对比最后合并为 str项.这个就和快排的思想一样

class Solution:
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x + pivot < pivot + x]
        mid = [x for x in arr if x + pivot == pivot + x]
        right = [x for x in arr if x + pivot > pivot + x]
        return self.quick_sort(left) + mid + self.quick_sort(right)
    def crackPassword(self, password: List[int]) -> str:
        # 1. 转换为字符串列表
        str_password = list(map(str, password))
        
        sorted_str_password = self.quick_sort(str_password)
        return "".join(sorted_str_password)