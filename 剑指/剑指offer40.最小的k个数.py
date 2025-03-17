"""
仓库管理员以数组 stock 形式记录商品库存表，其中 stock[i] 表示对应商品库存余量。请返回库存余量最少的 cnt 个商品余量，返回 顺序不限。

 

示例 1：

输入：stock = [2,5,7,4], cnt = 1
输出：[2]
示例 2：

输入：stock = [0,2,3,6], cnt = 2
输出：[0,2] 或 [2,0]
"""

# 排序stock，然后返回前cnt个数值
class Solution:
    def quick_sort(self, arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr)//2]
        left = [x for x in arr if x < pivot]
        mid = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return self.quick_sort(left) + mid + self.quick_sort(right)
    def inventoryManagement(self, stock: List[int], cnt: int) -> List[int]:
        arranged = self.quick_sort(stock)
        # 返回arranged的前cnt项的list
        return arranged[:cnt]