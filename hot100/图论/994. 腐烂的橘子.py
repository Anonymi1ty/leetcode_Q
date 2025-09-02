"""
在给定的 m x n 网格 grid 中，每个单元格可以有以下三个值之一：

值 0 代表空单元格；
值 1 代表新鲜橘子；
值 2 代表腐烂的橘子。
每分钟，腐烂的橘子 周围 4 个方向上相邻 的新鲜橘子都会腐烂。

返回 直到单元格中没有新鲜橘子为止所必须经过的最小分钟数。如果不可能，返回 -1 。

 

示例 1：

输入：grid = [[2,1,1],[1,1,0],[0,1,1]]
输出：4

"""

# 思路：
    # 和岛屿那个题目不同的是：多源（开始可能是多个橘子一起腐烂），并且只用广度优先遍历
    
    # 多源：把所有初始就腐烂的橘子同时作为 BFS 的起点（入队），它们能在 第 0 分钟 同时开始感染邻居。
    # 层次传播：每一轮从队列中弹出一批“当前时刻腐烂”的橘子，把它们四邻的新鲜橘子感染并入队，时间标记为 当前时间+1。
    # 计时方式：我们在入队时附带时间 t，或按层计数。每次感染产生的新腐烂橘子的时间就是 t+1，用 minutes 记录最大时间。
    # 判定不可能：BFS 结束仍有 fresh > 0，说明有新鲜橘子永远无法被感染（隔着空格或墙），返回 -1；否则返回 minutes。
    
from typing import List
from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        q = deque()         # 队列，存放当前已腐烂橘子的坐标 (r, c) 以及其腐烂发生的时间 t
        fresh = 0           # 新鲜橘子数量
        minutes = 0         # 传播所需的最小分钟数（最终答案）

        # 1) 预处理：统计新鲜橘子数量；把所有「初始就腐烂」的橘子入队，时间记为0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh += 1
                elif grid[r][c] == 2:
                    q.append((r, c, 0))  # (行, 列, 腐烂发生的时间)

        # 如果根本没有新鲜橘子，答案就是0
        if fresh == 0:
            return 0

        # 2) 多源BFS：从所有腐烂橘子同时出发，向四邻扩散
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        while q:
            r, c, t = q.popleft()
            # 尝试感染四个方向的新鲜橘子
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                # 越界判定 + 只有新鲜橘子(1)才会被感染
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    grid[nr][nc] = 2        # 被感染，变为腐烂
                    fresh -= 1              # 新鲜橘子数量-1
                    q.append((nr, nc, t+1)) # 这颗新烂橘子的时间 = 当前时间+1
                    minutes = t + 1         # 记录到目前为止所需的分钟数

        # 3) BFS结束后，如果还有新鲜橘子，说明存在无法被传播到的区域 → 返回 -1
        return -1 if fresh > 0 else minutes
