# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        p, q = min(p.val, q.val), max(p.val, q.val)

        def find_anc(root, p, q):
            if not root:
                return 0
            if root.val == p:
                return p
            elif root.val == q:
                return q
            elif p < root.val < q:
                return root.val
            
            return find_anc(root.left, p, q) + find_anc(root.right, p, q)

        return TreeNode(val=find_anc(root, p, q))
