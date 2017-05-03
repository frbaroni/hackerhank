    def getHeight(self,root):
        def fun(node, level):
            if node is None:
                return level
            else:
                left = fun(node.left, level + 1)
                right = fun(node.right, level + 1)
                return max(left, right)
        return fun(root, 0) - 1
