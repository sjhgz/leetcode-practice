#
# @lc app=leetcode.cn id=107 lang=python
#
# [107] 二叉树的层次遍历 II
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 思路： 使用队列进行广度优先遍历, 并且需要记录遍历节点的深度

class Solution(object):

    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        from collections import deque
        queue = deque()
        queue.appendleft((root, 0))  # 记录当前节点的深度
        res = []  # 输出结果的容器
        while queue:  # 循环遍历队列直到为空
            node, depth = queue.pop()
            last_depth = len(res)
            # 判断输出结果容器中最后一层的深度与当前节点的深度是否一致
            if last_depth - 1 == depth:  
                # 深度一致则直接添加追加
                layer = res[0]
                layer.append(node.val)
            else:
                res.insert(0, [node.val])
            if node.left:
                queue.appendleft((node.left, depth + 1))
            if node.right:
                queue.appendleft((node.right, depth + 1))
            
        return res
            

