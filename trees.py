class Node(object):
    def __init__(self, val):
        self.val = val
        self.right = None
        self.left = None


def in_order(root):
    if root is None:
        return
    in_order(root.left)
    print root.val
    in_order(root.right)


def pre_order(root):
    if root is None:
        return
    print root.val
    pre_order(root.left)
    pre_order(root.right)


def post_order(root):
    if root is None:
        return
    post_order(root.left)
    post_order(root.right)
    print root.val


def smallest_node(root):
    current = root
    while current.left:
        current = current.left
    return current


def biggest_node(root):
    current = root
    while current.right:
        current = current.right
    return current


def node_sum(node):
    if not node:
        return 0
    return node_sum(node.left) + node.val + node_sum(node.right)


def in_order_successor(root, target):
    if target.right:
        return smallest_node(target.right)

    succ = Node(None)

    while root:
        if target.val < root.val:
            succ = root
            root = root.left
        elif target.val > root.val:
            root = root.right
        else:
            break
    return succ


def collect(node, data, depth=0):
    if not node:
        return

    if depth not in data:
        data[depth] = [node.val]
    else:
        data[depth].append(node.val)

    collect(node.left, data, depth + 1)
    collect(node.right, data, depth + 1)


def avg_depth(root):
    data = {}
    collect(root, data)

    if not data:
        return

    result = []
    for val in data.values():
        result.append(sum(val) / len(val))

    return result


def height(node):
    if node is None:
        return 0
    else:
        return max(height(node.left), height(node.right)) + 1


def maxdepth(root):
    if not root:
        return 0

    left = maxdepth(root.left)
    right = maxdepth(root.right)

    return max(left, right) + 1


def isValidBST(root):
    def validate(node, lower=float("-inf"), upper=float("inf")):
        if not node:
            return True

        val = node.val
        if val <= lower or val >= upper:
            return False

        if not validate(node.right, val, upper):
            return False
        if not validate(node.left, lower, val):
            return False

        return True

    return validate(root)

import queue

def dfs_print(node):
    q = queue.Queue()
    if not node:
        return

    q.put(node)

    while not q.empty():
        node = q.get()
        if node:
            print node.val
            q.put(node.left)
            q.put(node.right)


def dfs_as_list(node):
    levels = []
    if not root:
        return levels
    
    def helper(node, level):
        # start the current level
        if len(levels) == level:
            levels.append([])

        # append the current node value
        levels[level].append(node.val)

        # process child nodes for the next level
        if node.left:
            helper(node.left, level + 1)
        if node.right:
            helper(node.right, level + 1)
        
    helper(root, 0)
    return levels


def rightView(root):
    # max_depth = -1
    right_view = dict()
    q = queue.Queue()
    q.put((root, 0), )  # put root in queue

    while not q.empty():
        node, depth = q.get()  # get from queue
        # max_depth = max(max_depth, depth)

        if node:
            right_view[depth] = node.val  # visit

            q.put((node.left, depth+1))  # enqueue
            q.put((node.right, depth+1))  # enqueue

    print right_view.values()


class Que:
    def __init__(self, ar):
        self.ar = ar or []

    def put(self, val):
        self.ar.append(val)

    def get(self):
        if self.ar:
            return self.ar.pop(0)


import collections

def verticalOrder(root):
    cols = collections.defaultdict(list)
    queue = [(root, 0)]
    for node, i in queue:
        if node:
            cols[i].append(node.val)
            queue += (node.left, i - 1), (node.right, i + 1)
    return [cols[i] for i in sorted(cols)]


def lca(root, p, q):
    if not root:
        return
    if root.val == p or root.val == q:
        return root

    right = lca(root.left, p, q)
    left = lca(root.right, q, p)

    if not right:
        return left
    elif not left:
        return right

    return root.val
    

def lcaBST(root, v1, v2):
    # Enter your code here
    if not root:
        return

    def helper(node):
        if v1 < node.val and v2 < node.val:  # nodes on left of root
            return helper(node.left)
        elif v1 > node.val and v2 > node.val:  # nodes on right of root
            return helper(node.right)
        else:
            return node

    return helper(root)

"""
                10                             [19, 22, 28, 30, 140, 130, 107, 100]
          /            \                
         5              35                   [9,12,18,20]             [90,97,120,130] 
       /   \          /     \
     3       7       30     45            [4,7]       [13,15]       [55,62]       [85,95]
   /   \   /   \   /   \   /   \          
  1     4 6     8 25   32 40   50       [1]    [4]   [6]    [8]    [25]   [32]   [40]  [50]
"""

max_sum = 0
def maxPathSum(root):
    """
    :type root: TreeNode
    :rtype: int
    """
    def max_gain(node):
        global max_sum
        if not node:
            return 0

        # max sum on the left and right sub-trees of node
        left_gain = max(max_gain(node.left), 0)
        right_gain = max(max_gain(node.right), 0)

        # the price to start a new path where `node` is a highest node
        price_newpath = node.val + left_gain + right_gain

        # update max_sum if it's better to start a new path
        max_sum = max(max_sum, price_newpath)

        # for recursion :
        # return the max gain if continue the same path
        return node.val + max(left_gain, right_gain)

    max_sum = float('-inf')
    max_gain(root)
    return max_sum


def main():
    root = Node(10)
    node5 = Node(5)
    node35 = Node(35)
    node3 = Node(3)
    node7 = Node(7)
    node30 = Node(30)
    node45 = Node(45)
    node1 = Node(1)
    node4 = Node(4)
    node6 = Node(6)
    node8 = Node(8)
    node25 = Node(25)
    node32 = Node(32)
    node40 = Node(40)
    node50 = Node(50)

    root.left = node5
    root.right = node35
    node5.left = node3
    node5.right = node7
    node35.left = node30
    node35.right = node45
    node3.left = node1
    node3.right = node4
    node7.left = node6
    node7.right = node8
    node30.left = node25
    node30.right = node32
    node45.left = node40
    node45.right = node50

    print maxdepth(root)

if __name__ == "__main__":
    main()