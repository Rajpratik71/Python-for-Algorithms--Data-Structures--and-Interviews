# vertices or nodes in a given graph
class  Node(object):
    def __init__(self , name):
        self.name = name                  # Name of Node
        self.adjacencyList = []           # Adjacency List
        self.visited = False              # Boolean check if visited node or not
        self.predecessor = None           # previous Vertex/Node in BFS
# Bredth First Search
class BredthFirstSearch(object):
    # startNode: Starting Node from where we need to start BFS
    def bfs(self,startNode):
        #For BFS, using Queue as ADT
        queue=[]
        #Initially , first value in the queue
        queue.append(startNode)
        #That node is visited, so true
        startNode.visited = True


        # while queue is not empty
        while queue:
            # actual node is the first node. FIFO Queue
            actualNode = queue.pop(0)
            print('%s'% actualNode.name)


            #visit all Neighbors of the current Node
            for n in actualNode.adjacencyList:
                #If Neighboring Node has not been visited, set visited to True and add to queue
                if not n.visited:
                    n.visited = True
                    queue.append(n)


#Testing
if __name__=='__main__':
    node1 = Node('Á')
    node2 = Node('B')
    node3 = Node('C')
    node4 = Node('D')
    node5 = Node('E')
    node6 = Node('F')

    node1.adjacencyList.append(node2)
    node1.adjacencyList.append(node3)
    node2.adjacencyList.append(node4)
    node4.adjacencyList.append(node5)
    node4.adjacencyList.append(node6)

    BFS = BredthFirstSearch()
    BFS.bfs(node1)

    # -------------------------- EOC --------------------------