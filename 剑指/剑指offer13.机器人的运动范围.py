"""
家居整理师将待整理衣橱划分为 m x n 的二维矩阵 grid，其中 grid[i][j] 代表一个需要整理的格子。整理师自 grid[0][0] 开始 逐行逐列 地整理每个格子。

整理规则为：在整理过程中，可以选择 向右移动一格 或 向下移动一格，但不能移动到衣柜之外。同时，不需要整理 digit(i) + digit(j) > cnt 的格子，其中 digit(x) 表示数字 x 的各数位之和。

请返回整理师 总共需要整理多少个格子。

 

示例 1：

输入：m = 4, n = 7, cnt = 5
输出：18

"""

# 思路：深度优先搜索（需要回溯，因为先下后右和先右后下返回结果一样）
    #如果越界或者超出范围返回False


class Solution:
    def wardrobeFinishing(self, m: int, n: int, cnt: int) -> int:
        self.res = 0
        # 用于记录每个格子是否已经访问过
        visited = [[False] * n for _ in range(m)]
        
        # 辅助函数：计算数字各位之和
        def digit_sum(x: int) -> int:
            s = 0
            while x:
                s += x % 10
                x //= 10
            return s
        
        def DFS(i: int, j: int):
            # 越界判断
            if i >= m or j >= n:
                return
            # 判断当前位置是否满足条件
            if digit_sum(i) + digit_sum(j) > cnt:
                return
            # 如果该格子已访问，直接返回避免重复计数
            if visited[i][j]:
                return
            
            # 标记为已访问并计数
            visited[i][j] = True
            self.res += 1
            
            # 只能向右和向下搜索
            DFS(i + 1, j)
            DFS(i, j + 1)
        
        DFS(0, 0)
        return self.res

