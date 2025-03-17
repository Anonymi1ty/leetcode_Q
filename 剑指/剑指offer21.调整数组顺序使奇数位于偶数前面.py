"""
教练使用整数数组 actions 记录一系列核心肌群训练项目编号。为增强训练趣味性，
需要将所有奇数编号训练项目调整至偶数编号训练项目之前。请将调整后的训练项目编号以 数组 形式返回。
"""

class Solution:
    def reorder_odd_even(self, arr: List[int]) -> List[int]:
        odd = [x for x in arr if x % 2 == 1]  # 取出所有奇数
        even = [x for x in arr if x % 2 == 0]  # 取出所有偶数
        return odd + even 
    def trainingPlan(self, actions: List[int]) -> List[int]:
        # 判断非空
        if not actions:
            return []
        return self.reorder_odd_even(actions)
