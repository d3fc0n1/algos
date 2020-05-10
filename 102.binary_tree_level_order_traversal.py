# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import queue
        q = queue.Queue()
        
        q.put((root, 0))
        result = [[]]
        level = 0
        
        while not q.empty():
            node, level = q.get()
            if not node:
                return
            if node.left:
                q.put((node.left, level+1))
            if node.right:
                q.put((node.right, level+1))
            
            if len(result) == level+1:
                result[level].append(node.val)
            else:
                result.append([node.val])
        
        return result