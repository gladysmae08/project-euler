class Node:
    def __init__(self, count=1):
        self.count = count
        self.children = {}

class Contacts:
    def __init__(self):
        self.Nodes = {}
        
    def add(self, name):
        current = self.Nodes
        for s in name:
            if s in current:
                current[s].count += 1
            else:
                current[s] = Node()
            current = current[s].children      

    def findPartial(self, part):
        current = self.Nodes
        for s in part[:-1]:
            if s in current:
                current = current[s].children
            else:
                return 0
        return current[part[-1]].count if part[-1] in current else 0

# read stdin
with open("contacts_input.txt") as f:
    lines = f.readlines()
contacts = Contacts()
fp = open("contacts_output.txt", 'w')
for x in lines[1:]:
    cmd, arg = (x.strip().split())
    if cmd == 'add':
        contacts.add(arg)
    else:
        fp.write(arg + ": " + str(contacts.findPartial(arg)) + '\n')
fp.close()