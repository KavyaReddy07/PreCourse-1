# Python program to insert element in binary tree  
class newNode():  
  
    def __init__(self, data):  
        self.key = data 
        self.left = None
        self.right = None
          
""" Inorder traversal of a binary tree"""
def inorder(temp):

    curr = temp
    stack = []
    while True:
        if curr:
            stack.append(curr)
            curr = curr.left
        elif stack:
            left = stack.pop()
            print(left.key)
            curr = left.right
        else:
            break


"""function to insert element in binary tree """
def insert(temp, key):
    if not temp:
        root = newNode(key)
        return
    currList = []
    currList.append(temp)

    while len(currList):
        curr = currList[0]
        currList.pop(0)
        if curr.left:
            currList.append(curr.left)
        else:
            print('In l', curr.key)
            curr.left = newNode(key)
            break
        if curr.right:
            currList.append(curr.right)
        else:
            print('In r', curr.key)
            curr.right = newNode(key)
            break

# Driver code  
if __name__ == '__main__': 
    root = newNode(10)  
    root.left = newNode(11)  
    root.left.left = newNode(7)  
    root.right = newNode(9)  
    root.right.left = newNode(15)  
    root.right.right = newNode(8)  
  
    print("Inorder traversal before insertion:", end = " ") 
    inorder(root)  
  
    key = 12
    insert(root, key)  
  
    print()  
    print("Inorder traversal after insertion:", end = " ") 
    inorder(root) 
