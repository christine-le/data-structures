# Trees and Graphs exercises (from Cracking The Coding Interview)

# Practice
class TreeNode(object):
    def __init__ (self, data):
        self.data = data
        self.left = None
        self.right = None

class Tree(object):
    def __init__ (self):
        self.root = None

    def insert(self, val):
        if self.root == None:
            self.root = TreeNode(val)
            return self.root

        curr = self.root
        while curr != None:
            if val < curr.data:
                if curr.left != None:
                    curr = curr.left
                else:
                    curr.left = TreeNode(val)
                    break
            if val > curr.data:
                if curr.right != None:
                    curr = curr.right
                else:
                    curr.right = TreeNode(val)
                    break
        return self.root

    def print_tree(self):
        children = [self.root]

        while len(children) > 0:
            temp = []
            for i in children:
                print i.data,
                if i.left != None:
                    temp.append(i.left)
                if i.right != None:
                    temp.append(i.right)
            children = temp

tree = Tree()
tree.insert(4)
tree.insert(7)
tree.insert(5)
# tree.print_tree()
print ""
tree2 = Tree()
tree2.insert_rec(4)
tree2.insert_rec(7)
tree2.insert_rec(5)
tree2.print_tree()

