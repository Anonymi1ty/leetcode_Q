"""
给你一个整数数组 nums，返回 数组 answer ，其中 answer[i] 等于 nums 中除 nums[i] 之外其余各元素的乘积 。

题目数据 保证 数组 nums之中任意元素的全部前缀元素和后缀的乘积都在  32 位 整数范围内。

请 不要使用除法，且在 O(n) 时间复杂度内完成此题。

 

示例 1:

输入: nums = [1,2,3,4]
输出: [24,12,8,6]
示例 2:

输入: nums = [-1,1,0,-3,3]
输出: [0,0,9,0,0]
 
"""

# 思路：(可以看看 https://leetcode.cn/problems/product-of-array-except-self/solutions/11472/product-of-array-except-self-shang-san-jiao-xia-sa/ 的评论)
    # 当前位置的结果就是它左部分的乘积再乘以它右部分的乘积。
    # 因此需要进行两次遍历，第一次遍历用于求左部分的乘积，第二次遍历在求右部分的乘积的同时，再将最后的计算结果一起求出来。
from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        # answer[i] 将先存储 nums[0..i-1] 的前缀乘积
        answer = [1] * n
        
        # 1) 计算前缀乘积
        prefix = 1
        for i in range(n):
            answer[i] = prefix
            prefix *= nums[i]
        
        # 2) 计算后缀乘积并乘到 answer 中
        suffix = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= suffix
            suffix *= nums[i]
        
        return answer

if __name__ == "__main__":
    # 读取输入：一行，格式如 [1,2,3,4]
    import sys, ast
    line = sys.stdin.readline().strip()
    nums = ast.literal_eval(line)  # 安全地将输入字符串转为列表
    res = Solution().productExceptSelf(nums)
    # 输出结果列表
    print(res)
