#
# @lc app=leetcode.cn id=104 lang=python
#
# [104] 二叉树的最大深度
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 思路： 使用递归的方式进行解题, 通常来说，涉及到树的操作用递归
# 会比较清晰明了，也可以用栈或者队列进行模拟

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        depth = 1
        depth = self._max_depth(root.left, root.right, depth)
        return depth
        
    def _max_depth(self, p, q, depth):

        if not p and not q:
            return depth
        depth += 1
        depth_1  = 0 # 初始化变量, 左子树的初始深度
        depth_2 = 0 # 初始化变量, 右子树的初始深度
        if p:
            depth_1 = self._max_depth(p.left, p.right, depth)
        if q:
            depth_2 = self._max_depth(q.left, q.right, depth)
        if depth_1  >= depth_2:
            if depth_1 > depth:
                return depth_1
            return depth
        else:
            if depth_2 > depth:
                return depth_2
            return depth
            
        
