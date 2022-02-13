from .node import Node

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break

    def getHeight(self):
        return self.__countHeight(self.root)

    def __countHeight(self, root):

        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        heightRight =+ self.__countHeight(root.right)
        heightleft =+ self.__countHeight(root.left)

        return max(heightRight, heightleft) + 1
