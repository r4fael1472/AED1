class Node:
    def __init__(self, data):
        self.data = data
        self.right_child = None
        self.left_child = None


def inorder(root_node):
    current = root_node
    if current is None:
        return
    inorder(current.left_child)
    print(current.data)
    inorder(current.right_child)


nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")
nE = Node("E")

nA.right_child = nC
nA.left_child = nB
nB.right_child = nE
nB.left_child = nD

inorder(nA)
