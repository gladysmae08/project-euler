# find largest path in binary tree

def readTree(file):
    tree = []
    with open(file) as fp:
        for line in fp.readlines():
            ints = list(map(int, line.split()))
            tree.append(ints)
    return tree

def findMaxPath(tree):
    tree = tree[:]
    bottom = len(tree) - 2
    for i in range(bottom, -1, -1):
        for index, node in enumerate(tree[i]):
            tree[i][index] = node + max(tree[i+1][index], tree[i+1][index+1])
    return tree[0][0]
    
tree = readTree('problem67_input.txt')
print(findMaxPath(tree))