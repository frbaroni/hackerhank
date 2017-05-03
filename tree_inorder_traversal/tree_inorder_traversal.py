"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def fun(root):
    items = []
    if root is not None:
        items.extend(fun(root.left))
        items.append(root.data)
        items.extend(fun(root.right))
    return items

def inOrder(root):
    values = map(str, fun(root))
    print(" ".join(values))
    
