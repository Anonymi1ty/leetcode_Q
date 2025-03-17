#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# 使用双指针的话分析题目，可以从后往前做
# @lc code=start
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 特殊情况，nums1为空
        if m < 1:
            # python 拷贝不能直接使用nums1 = nums2，这样的赋值操作实际上是创建了一个新的列表对象
            nums1[:n] = nums2
            return
            
        res_temp = []
        head_1 = head_2 =0
        while head_1 < m and head_2 < n:
            # 左边的一组小于右边的
            if nums1[head_1] <= nums2[head_2]:
                # 加入左边的
                res_temp.append(nums1[head_1])
                # 移动左指针
                head_1 += 1
            else:
                # 加入右边的
                res_temp.append(nums2[head_2])
                head_2 += 1
        # 左边有剩余的加入
        res_temp += nums1[head_1: m]
        # 右边有剩余的加入
        res_temp += nums2[head_2: n]
        # 赋值
        nums1[:m+n] = res_temp
        
                
            
        
# @lc code=end

