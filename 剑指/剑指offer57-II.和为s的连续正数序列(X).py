"""
待传输文件被切分成多个部分，按照原排列顺序，每部分文件编号均为一个 正整数（至少含有两个文件）。传输要求为：连续文件编号总和为接收方指定数字 target 的所有文件。请返回所有符合该要求的文件传输组合列表。

注意，返回时需遵循以下规则：

每种组合按照文件编号 升序 排列；
不同组合按照第一个文件编号 升序 排列。
 

示例 1：

输入：target = 12
输出：[[3, 4, 5]]
解释：在上述示例中，存在一个连续正整数序列的和为 12，为 [3, 4, 5]。
示例 2：

输入：target = 18
输出：[[3,4,5,6],[5,6,7]]
解释：在上述示例中，存在两个连续正整数序列的和分别为 18，分别为 [3, 4, 5, 6] 和 [5, 6, 7]。

1 <= target <= 10^5
"""

# 思路：初始化一个顺序的list，使用滑动窗口来进行计算
    # 循环： 当 i≥j 时跳出；
        # 当 s>target 时： 向右移动左边界 i=i+1 ，并更新元素和 s ；
        # 当 s<target 时： 向右移动右边界 j=j+1 ，并更新元素和 s ；
        # 当 s=target 时： 记录连续整数序列，并向右移动左边界 i=i+1 ；

class Solution:
    def fileCombination(self, target: int) -> List[List[int]]:
        left, right = 1, 2
        sum = 3
        res = []
        
        while left < right:
            if sum == target:
                res.append(list(range(left, right + 1)))
                sum -= left  # 关键：确保 `left` 指针也移动
                left += 1
            elif sum < target:
                right += 1
                sum += right
            else:  # `elif sum > target:` 的情况可以直接用 `else`
                sum -= left
                left += 1

        return res
        