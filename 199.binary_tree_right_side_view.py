class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        # normal BFS level-order as list of lists
        import queue
        q = queue.Queue()
        q.put((root, 0))
        result = [[]]

        while not q.empty():
            if not node:
                return
            node, level = q.get()
            if node.left:
                q.put((node.left, level + 1))
            if node.right:	
                q.put((node.right, level + 1))

            if level == len(result) - 1:
                result[level].append(node.val)
            else:
                result.append([node.val])

        return [x[-1] for x in result]

        # # using hashmap to record last value at depth
        # import queue
        # q = queue.Queue()
        # q.put((root, 0))
        # rightview = {}
        # while not q.empty():
        #     node, depth = q.get()
        #     if node:
        #         rightview[depth] = node.val
        #         if node.left:
        #             q.put((node.left, depth+1))
        #         if node.right:
        #             q.put((node.right, depth+1))
        # return rightview.values()