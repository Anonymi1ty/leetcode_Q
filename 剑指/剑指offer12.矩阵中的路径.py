"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true

"""

# 思路：深度优先搜索
    #每次对四个方向进行搜索，如果越界或者不匹配返回False，四个方向都为False，总体为False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        
        
        def dfs(i, j, k):
            # 如果匹配完成，返回 True
            if k == len(word):
                return True
            # 越界或字符不匹配，返回 False
            if i < 0 or i >= m or j < 0 or j >= n or board[i][j] != word[k]:
                return False
            
            # 临时标记当前单元格为已访问（例如赋予特殊字符）
            temp = board[i][j]
            board[i][j] = '#'
            
            # 四个方向继续搜索
            found = (dfs(i + 1, j, k + 1) or
                     dfs(i - 1, j, k + 1) or
                     dfs(i, j + 1, k + 1) or
                     dfs(i, j - 1, k + 1))
            
            # 恢复当前单元格的值（回溯）
            board[i][j] = temp
            return found
        
        # 从每个单元格出发进行 DFS 搜索
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False