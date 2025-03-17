#
# @lc app=leetcode id=909 lang=python3
#
# [909] Snakes and Ladders
#

# 二维矩阵是乱序的，我们需要将其转化为一维数组，然后进行BFS遍历（每一步最多走6步，将每一步的结果加入队列中，然后再进行下一步的遍历）
    # 不用记录每一个点的最短路径的原因是：如果从起点到终点的最短路径是通过某个点的，那么从起点到这个点的最短路径也是通过这个点的，所以我们只需要记录每一个点是否被访问过即可
    # 在最短路径被找到时，其他还在队列中的点就不需要再继续遍历了，因为这些点的最短路径一定比当前的最短路径要长
# @lc code=start
import queue
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        # 首先将二维数组转化为一维数组
        n = len(board)
        # nums存储一维数组
        nums = [0]
        # flag表示是否从左到右
        flag = True
        # i从n-1到0，每次减1
        for i in range(n-1, -1, -1):
            if flag:
                # 加入第i行的元素
                nums += board[i]
            # 如果不是从左到右，就将board[i]反转
            else:
                # [::-1]表示start 和 stop 都没有指定，因此默认从序列的开头到结尾,-1表示步长为-1，即从右到左
                nums += board[i][::-1]
            flag = not flag
            
    
        # 初始化一个队列
        q = queue.Queue()
        # 初始化一个set
        visited = set()
        # 起始点为1
        q.put(1)
        visited.add(1)
        # 步数为0
        step = 0
        # BFS 遍历
        while not q.empty():
            for _ in range(q.qsize()):
                node = q.get()
                if node == n * n:  # 到达终点
                    return step
                for i in range(1, 7):  # 模拟骰子，最多可以走6步
                    next_pos = node + i
                    if next_pos > n * n:  # 超出棋盘
                        continue
                    
                    # 根据蛇梯子或普通格子进行跳跃或移动
                    final_pos = nums[next_pos] if nums[next_pos] != -1 else next_pos
                    
                    # 如果没访问过该格子，则加入队列
                    if final_pos not in visited:
                        visited.add(final_pos)
                        q.put(final_pos)
            # 在操作最后，步数加1（如果提前step += 1，会导致最后一步多加一次）
            step += 1
        return -1  # 如果无法到达终点，则返回 -1
        
# @lc code=end

