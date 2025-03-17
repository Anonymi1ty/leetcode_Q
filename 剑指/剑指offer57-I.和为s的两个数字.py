"""
购物车内的商品价格按照升序记录于数组 price。请在购物车中找到两个商品的价格总和刚好是 target。若存在多种情况，返回任一结果即可。

示例 1：

输入：price = [3, 9, 12, 15], target = 18
输出：[3,15] 或者 [15,3]
示例 2：

输入：price = [8, 21, 27, 34, 52, 66], target = 61
输出：[27,34] 或者 [34,27]
"""

# 思路：有序数组，并且是查找问题，首先想到二分（把这个题变为二分即可）
    # 开始固定一个数字，然后二分查找另一个即可
# 或者双指针（更简单一些）
class Solution:
    def binary_search(self, arr, target, left):
        right = len(arr) - 1
        while left <= right: 
            mid = left + (right - left)//2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    def twoSum(self, price: List[int], target: int) -> List[int]:
        if not price:
            return
        for i in range(0, len(price) -1):
            candidate = price[i]
            find = target - candidate
            # 判断是否能找到,在 i+1 之后的范围内查找避免查找到自己
            flag = self.binary_search(price, find, i+1)
            if flag:
                return [candidate, find]
        return
