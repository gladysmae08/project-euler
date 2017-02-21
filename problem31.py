from timeit import default_timer

coins = [1, 2, 5, 10, 20, 50, 100, 200]

class Node:
    def __init__(self, value):
        self.edges = []
        self.setEdges(value)
    def setEdges(self, value):
        for coin in coins:
            if value - coin >= 0:
                self.edges.append((coin, value-coin))

def traverse(index, max, nodes):
    if (index == 0): return 1
    else:
        sum = 0
        for edge in nodes[index].edges:
            if edge[0] >= max:
                sum += traverse(edge[1], edge[0], nodes)
    return sum

if __name__ == "__main__":
   
    start = default_timer()
    nodes = []
    for i in range(0,201):
        nodes.append(Node(i))
    sum = traverse(200, 0, nodes)
    time = default_timer() - start 
    print("Count: %s" % sum)
    print("Time: %s" % time)


