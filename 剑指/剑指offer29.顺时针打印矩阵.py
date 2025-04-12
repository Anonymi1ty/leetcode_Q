"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
"""

# 思路：记录矩阵行长度 wide = len(matrix[0]) len = len(matrix) visited = {(m,n)};按照右->下->左->上的顺序循环

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 如果矩阵为空或者第一行为空，则直接返回空列表
        if not matrix or not matrix[0]:
            return []
        
        m, n = len(matrix), len(matrix[0])  # m为矩阵的行数，n为矩阵的列数
        total = m * n                      # 记录矩阵中元素的总数
        visited = set()                    # 用于存储访问过的坐标 (i, j)
        res = []                           # 保存遍历结果
        
        # 定义顺时针遍历的四个方向：
        # 向右：(0, 1)
        # 向下：(1, 0)
        # 向左：(0, -1)
        # 向上：(-1, 0)
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir_index = 0  # 当前方向的索引，初始方向为向右
        
        # 从矩阵左上角开始遍历
        i, j = 0, 0
        
        # 当结果列表中记录的元素个数小于总数时，继续循环
        while len(res) < total:
            # 访问当前元素，并将其加入结果列表，同时记录当前坐标为已访问
            res.append(matrix[i][j])
            visited.add((i, j))
            
            # 计算沿当前方向前进一步后的新坐标
            next_i = i + directions[dir_index][0]
            next_j = j + directions[dir_index][1]
            
            # 判断下一个位置是否有效：
            # 1. 必须在矩阵范围内
            # 2. 该位置还没有被访问过;continue
            
            # 如果不满足，则转向
            if not (0 <= next_i < m and 0 <= next_j < n) or ((next_i, next_j) in visited):
                # 如果无效，则改变方向（顺时针旋转，方向索引加1，取模4保证循环）
                dir_index = (dir_index + 1) % 4
                # 更新下一个位置，新方向下的坐标
                next_i = i + directions[dir_index][0]
                next_j = j + directions[dir_index][1]
            
            # 移动到下一个位置
            i, j = next_i, next_j
        
        return res
                