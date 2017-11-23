class Node:
    def __init__(self, val):
        self.data = val
        self.left_node = None
        self.right_node = None

    def insert(self, val):
        if self.data == val:
            return False
        elif self.data > val:
            if self.left_node is not None:
                self.left_node.insert(val)
            else:
                self.left_node = Node(val)
        elif self.data < val:
            if self.right_node is not None:
                self.right_node.insert(val)
            else:
                self.right_node = Node(val)

    def find(self, val):
        if self.data == val:
            return True
        if self.data > val:
            if self.left_node is not None:
                return self.left_node.find(val)
            else:
                return False
        else:
            if self.right_node is not None:
                return self.right_node.find(val)
            else:
                return False

    def preorder(self):
        print self.data
        if self.left_node:
            self.left_node.preorder()
        if self.right_node:
            self.right_node.preorder()

    def inorder(self):
        if self.left_node:
            self.left_node.inorder()
        print self.data
        if self.right_node:
            self.right_node.inorder()

    def postorder(self):
        if self.left_node:
            self.left_node.postorder()
        if self.right_node:
            self.right_node.postorder()
        print self.data
         
    def bfs(self, queue):
        print self.data
        queue.append(self.left_node)
        queue.append(self.right_node)

    def get_data(self):
        return self.data

    def get_left_node(self):
        return self.left_node

    def get_right_node(self):
        return self.right_node

   
class Tree:
    def __init__(self):
        self.root = None
        self.queue = []
        
    def insert(self, val):
        if self.root == None:
            self.root = Node(val)
            self.queue.append(self.root)
        else:
            self.root.insert(val)

    def find(self, val):
        return self.root.find(val)

    def preorder(self):
        self.root.preorder()

    def postorder(self):
        self.root.postorder()

    def inorder(self):
        self.root.inorder()

    def bfs(self):
        node = self.queue.pop(0)
        print node.get_data()
        if node.get_left_node() is not None:
            self.queue.append(node.get_left_node())
        if node.get_right_node() is not None:
            self.queue.append(node.get_right_node())
        if self.queue:
            self.bfs()
