"""

Created by Avi.Kumar on 6/15/2018
Copyright : Aviral (Avi) Kumar

"""
class Node():
    def __init__(self, val):
        self.left = None
        self.right = None
        self.data = val

class BST():
    def __init__(self):
        self.root = None
        self.size = 0

    def searchNode(self,currentNode, key):
        # Searches a given key in the tree
        if currentNode is None:
            return False
        elif currentNode.data == key:
            return True

        elif currentNode.data < key:
            return self.searchNode(currentNode.right, key)

        else:
            return self.searchNode(currentNode.left, key)

    def search(self, val):
        return self.searchNode(self.root, val)

    def setRoot(self, val):
        self.root = Node(val)

    def insertNode(self,currentnode,val):
        if val <= currentnode.data :
            if currentnode.left :
                self.insertNode(currentnode.left, val)
            else:
                currentnode.left = Node(val)

        elif (val > currentnode.data):
            if (currentnode.right) :
                self.insertNode(currentnode.right, val)
            else:
                currentnode.right = Node(val)

    def delete(self, val):
        if self.root is None:
            print "Empty BST"
        else:
            self.deleteNode(self.root, val)

    def minNode(self, node):
        current = node

        while (current.left is not None):
            current = current.left

        return current

    def deleteNode(self, currentNode, val):
        if currentNode is None :
            return currentNode
        if currentNode.data < val:
            currentNode.right = self.deleteNode(currentNode.right, val)
        elif currentNode.data > val :
            currentNode.left = self.deleteNode(currentNode.left, val)

        else :
            if currentNode.left is None:
                temp = currentNode.right
                currentNode = None
                return temp

            elif currentNode.right is None:
                temp = currentNode.left
                root = None
                return temp

            temp = self.minNode(currentNode.right)

            currentNode.data = temp.data

            currentNode.right = self.deleteNode(currentNode.right, temp.data)



    def insert(self, val):
        if self.root is None:
            self.setRoot(val)
        else:
            self.insertNode(self.root, val)

    def inorder(self):
        if self.root:
            self.inorder_disp(self.root)
        else:
            print "Empty"

    def inorder_disp(self, currentNode):
        if currentNode:
            self.inorder_disp(currentNode.left)
            print currentNode.data
            self.inorder_disp(currentNode.right)

    def Print(self, currentNode, n1, n2):
        if currentNode is None:
            return currentNode
        if n1 < currentNode.data:
            self.Print(currentNode.left, n1, n2)

        if n1 <= currentNode.data and n2 >= currentNode.data:
            print currentNode.data

        if n2 > currentNode.data:
            self.Print(currentNode.right, n1, n2)

    def printRange(self, n1, n2):
        if self.root is None :
            return self.root
        else:
            self.Print(self.root, n1, n2)
if __name__ == "__main__":
    tree = BST()
    tree.insert(5)
    tree.insert(6)
    tree.insert(9)
    tree.insert(4)
    print tree.search(4)
    tree.inorder()
    tree.delete(5)
    print "*****"
    tree.inorder()
    print "*******"
    tree.printRange(5,10)
