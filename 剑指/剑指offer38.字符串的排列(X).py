"""
某店铺将用于组成套餐的商品记作字符串 goods，其中 goods[i] 表示对应商品。请返回该套餐内所含商品的 全部排列方式 。

返回结果 无顺序要求，但不能含有重复的元素。

 

示例 1：

输入：goods = "agew"
输出：["aegw","aewg","agew","agwe","aweg","awge","eagw","eawg","egaw","egwa","ewag",
       "ewga","gaew","gawe","geaw","gewa","gwae","gwea","waeg","wage","weag","wega","wgae","wgea"]
"""

# 思路：使用DFS（比如上面的例子，第一个是a，那么剩下的组合是3*2*1，是不是和DFS思路一样）

class Solution:
    def goodsOrder(self, goods: str) -> List[str]:
        arr = list(goods)
        res = []
        def dfs(x):
            if x == len(arr) - 1:
                res.append(''.join(arr))
                return
            # 使用set 可以防止重复，达到题目要求
            visited = set()
            for i in range(x, len(arr)):
                if arr[i] in visited:
                    continue
                visited.add(arr[i])
                # i 和 x排列换位置
                    #第一次循环，1和1换位置，2和2换位置...
                    #第二次循环，1和2换位置，2和2换位置...
                arr[x], arr[i] = arr[i], arr[x]
                # 递归固定下一个位置(深度优先，它会便利完所有的该分支下的可能)
                dfs(x + 1)
                # 回溯，恢复原来的排列顺序
                arr[x], arr[i] = arr[i], arr[x]
        dfs(0)
        return res