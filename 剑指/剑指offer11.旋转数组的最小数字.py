"""
已知一个长度为 n 的数组，预先按照升序排列，经由 1 到 n 次 旋转 后，得到输入数组。例如，原数组 nums = [0,1,2,4,5,6,7] 在变化后可能得到：
若旋转 4 次，则可以得到 [4,5,6,7,0,1,2]
若旋转 7 次，则可以得到 [0,1,2,4,5,6,7]
注意，数组 [a[0], a[1], a[2], ..., a[n-1]] 旋转一次 的结果为数组 [a[n-1], a[0], a[1], a[2], ..., a[n-2]] 。

给你一个元素值 互不相同 的数组 nums ，它原来是一个升序排列的数组，并按上述情形进行了多次旋转。请你找出并返回数组中的 最小元素 。

你必须设计一个时间复杂度为 O(log n) 的算法解决此问题。
"""

# 个人思路：因为时间复杂度被规定为O(log n)，直接使用快排暴力破解也可以。最好使用二分查找（技巧）
from typing import List


class Solution:
    # self是为了方便调用类中的函数
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1          # 左闭右闭区间，如果用右开区间则不方便判断右值
        while left < right:                     # 循环不变式，如果left == right，则循环结束
            mid = left + (right - left )/2      
            if nums[mid] > nums[right]:         # 中值 > 右值，左半边有序，最小值在右半边，收缩左边界
                left = mid + 1                  # 因为中值 > 右值，中值肯定不是最小值，左边界可以跨过mid
            elif nums[mid] < nums[right]:       # 明确中值 < 右值，右半边有序，最小值在左半边，收缩右边界
                right = mid                     # 因为中值 < 右值，中值也可能是最小值，右边界只能取到mid处
        return nums[left]                       # 循环结束，left == right，最小值输出nums[left]或nums[right]均可
    