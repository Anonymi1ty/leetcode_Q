"""
你这个学期必须选修 numCourses 门课程，记为 0 到 numCourses - 1 。

在选修某些课程之前需要一些先修课程。 先修课程按数组 prerequisites 给出，其中 prerequisites[i] = [ai, bi] ，表示如果要学习课程 ai 则 必须 先学习课程  bi 。

例如，先修课程对 [0, 1] 表示：想要学习课程 0 ，你需要先完成课程 1 。
请你判断是否可能完成所有课程的学习？如果可以，返回 true ；否则，返回 false 。

 

示例 1：

输入：numCourses = 2, prerequisites = [[1,0]]
输出：true
解释：总共有 2 门课程。学习课程 1 之前，你需要完成课程 0 。这是可能的。
示例 2：

输入：numCourses = 2, prerequisites = [[1,0],[0,1]]
输出：false
解释：总共有 2 门课程。学习课程 1 之前，你需要先完成​课程 0 ；并且学习课程 0 之前，你还应先完成课程 1 。这是不可能的。

"""

# 思路：
    # 有向图不能成环
    # 入度 indeg[i]：课程 i 还需多少门先修课没完成。
    # 初始化队列：把所有入度为 0 的课入队（可以马上学）。
    # BFS 过程：每学完一门课，就“释放”它指向的后继课（入度减 1）；若某后继课入度降为 0，则入队。
    # 判定：最终能弹出的课程数等于总数 ⇒ 无环 ⇒ 可以学完；否则图中存在环 ⇒ 不可行
    
from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # 建邻接表与入度数组
        graph = [[] for _ in range(numCourses)]
        indeg = [0] * numCourses # 初始化所有课的入度
        for a, b in prerequisites:
            graph[b].append(a)  # b -> a
            indeg[a] += 1

        # 入度为 0 的点（无前置课）先入队
        q = deque([i for i in range(numCourses) if indeg[i] == 0])
        learned = 0  # 计数已“学完”的课程数（拓扑序长度）

        while q:
            u = q.popleft()
            learned += 1
            # “学习”u 后，它指向的课程入度减 1
            for v in graph[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)

        # 若能弹出所有课程，说明无环；否则有环
        return learned == numCourses
