class Node:
    def __init__(self, val):
        self.left = None
        self.right = None
        self.v = val


class Tree:
    def __init__(self):
        self.root = None

    def getRoot(self):
        return self.root

    def add(self, val):
        if self.root is None:
            self.root = Node(val)
        
        else:
            self._add(val, self.root)

    def _add(self,val,node):
        if val < node.v:
            if node.left is not None:
                self ._add(val, node.left)
            else:
                node.left = Node(val)
        
        else:
            if node.right is not None:
                self ._add(val, node.right)
            else:
                node.right = Node(val)

    def find(self,val):
        if self.root is not None:
            return self._find(val, self.root)

    def _find(self,val, node):
        if val == node.v:
            