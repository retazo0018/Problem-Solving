class Tree:
    def __init__(self,data=None):
        self.data = data
        self.children = []
    def root(self,data):
        self.root = data
    def add(self,node):
        self.children.append(node)
    def search(self,data):
        if(self.data == data):
            return self
        else:
            for child in self.children:
                t = child.search(data)
                if(t is not None):
                    return t
            return None
    def bfs(self):
        queue = [self]
        level = []
        temp = []
        temp.append(self.data)
        level.append(temp)
        temp=[]
        while(queue !=[]):
            pop = queue.pop(0)
            for child in pop.children:
                queue.append(child)
                temp.append(child.data)
            if(len(temp)>0):
                level.append(temp)
            temp=[]
            print(pop.data,end=" ")
            
        return(level)
tree = None
print("Menu\n 1. Add a root node 2. Add as a child of a parent node 3. Exit")
getInput = input()
while(True):
    if(getInput=='1'):
        n = int(input("Enter the root node value: "))
        new_node = Tree(n)
        new_node.root(n)
        tree = new_node
    elif(getInput=='2'):
        key = int(input("Enter the parent node: "))
        n = int(input("Enter the node value: "))
        new_node = Tree(n)
        ref = None
        if(tree is not None):
            ref = tree.search(key)
        if(ref==None):
            print("Node not found.")
            continue
        ref.add(new_node)
        bfschoice = input("Do you want to perform bfs of the tree? Y|n ")
        if(bfschoice=='Y'):
            print("BFS traversal: ")
            level = tree.bfs()
            print()
            for i in range(len(level)):
                print("Level "+str(i+1)+" nodes: ", end=" ")
                for j in range(len(level[i])):
                    print(level[i][j],end=" ")
                print()
    elif(getInput=='3' or getInput=='n'):
        break
    else:
        print("Invalid option.")
    getInput = input("Enter the choice 1|2|3 : ")
