tree = Tree()
tree.add(3)
tree.add(9)
tree.add(20)
tree.add(None)
tree.add(None)
tree.add(15)
tree.add(7)



def levelOrder(root):
    if not root:
        return []
    a = [root]
    res = []
    j = 0
    while a:
        b = []
        for i in range(len(a)):
            n = a.pop(0)
            if n :
                b.append(n.val)
                if n.left:
                    a.append(n.left)
                if n.right:
                    a.append(n.right)
        if j % 2 == 0:
            res.append(b)
        else:
            res.append(b[::-1])
        j += 1
    return res


print(levelOrder(tree.root))