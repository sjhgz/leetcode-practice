#
# @lc app=leetcode.cn id=101 lang=python
#
# [101] 对称二叉树
#
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return True
        return self._is_symmetric(root.left, root.right)
    
    def _is_symmetric(self, p, q):
        
        if not p and not q:
            return True
        if not p or not q:
            # 注意这个条件分支跟上一个条件分支的顺序不能互换
            return False 
        if p.val != q.val:
            return False
        return self._is_symmetric(p.left, q.right) and \
            self._is_symmetric(p.right, q.left)
            
