"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.data (the value of the node)
"""
def fun(root):
    items = []
    if root is not None:
        items.append(root.data)
        items.extend(fun(root.left))
        items.extend(fun(root.right))
    return items

def preOrder(root):
    values = map(str, fun(root))
    print(" ".join(values))
    
