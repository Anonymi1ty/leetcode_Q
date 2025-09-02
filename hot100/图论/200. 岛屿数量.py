"""
给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。

岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。

此外，你可以假设该网格的四条边均被水包围。

 

示例 1：

输入：grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
输出：1

"""

# 思路：
    # 深度优先搜索（DFS）
    # 遍历每个格子：如果遇到 '1'（陆地），说明发现了一个新的岛屿。
    # 启动 DFS：从这个格子开始，将它连接的所有陆地（上下左右）都淹没（置为 '0'），保证这块陆地不会被重复计算。
    # 计数：每次启动 DFS，说明发现了一座新的岛屿，所以 count += 1。
    # 最终返回 count，就是岛屿数量
    
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        # 定义深度优先搜索函数
        def dfs(grid, i, j):
            # 递归终止条件：
            # 1. 越界（i 或 j 不在合法范围内）
            # 2. 遇到水格子（'0'）
            if not 0 <= i < len(grid) or not 0 <= j < len(grid[0]) or grid[i][j] == '0':
                return
            
            # 将当前陆地标记为水，避免重复访问
            grid[i][j] = '0'
            
            # 向上下左右四个方向继续搜索
            dfs(grid, i + 1, j)  # 下
            dfs(grid, i, j + 1)  # 右
            dfs(grid, i - 1, j)  # 上
            dfs(grid, i, j - 1)  # 左

        count = 0  # 记录岛屿数量
        # 遍历整个网格
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # 遇到陆地（'1'）时，启动一次 DFS
                if grid[i][j] == '1':
                    dfs(grid, i, j)  # 将该岛屿的所有陆地淹没
                    count += 1       # 岛屿数量加一
        return count

from collections import deque

# 广度优先遍历BFS版本
class Solution:
    def numIslands(self, grid: [[str]]) -> int:
        if not grid:  # 特殊情况：空网格
            return 0
        
        rows, cols = len(grid), len(grid[0])
        count = 0  # 记录岛屿数量

        def bfs(i, j):
            # 创建队列，把当前陆地位置放入队列
            queue = deque()
            queue.append((i, j))
            # 将该位置标记为 '0'，表示已访问
            grid[i][j] = '0'

            # BFS 遍历
            while queue:
                x, y = queue.popleft()
                # 遍历上下左右四个方向
                for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
                    nx, ny = x + dx, y + dy
                    # 检查是否越界 & 是否是陆地
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == '1':
                        queue.append((nx, ny))   # 新的陆地加入队列
                        grid[nx][ny] = '0'       # 同时淹没，避免重复访问

        # 遍历每个格子
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '1':   # 遇到新岛屿
                    bfs(i, j)           # 用 BFS 把整座岛屿淹没
                    count += 1          # 岛屿数加 1

        return count
