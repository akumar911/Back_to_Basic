"""

Created by Avi.Kumar on 7/2/2018
Copyright : Aviral (Avi) Kumar

"""


class GraphADT:
    '''
    Creates an Undirected Graph of the capacity given by the User.
    '''
    def __init__(self, capacity):

        self.capacity = capacity
        self.vertices = []

        self.adjacency_matrix = [[0 for x in range(capacity)] for y in range(capacity)]

        self.used= []

    def addVertex(self, v):
        self.vertices.append(v)

    def removeVertex(self, v):
        self.vertices.remove(v)

    def addEdge(self, start, end):

        self.adjacency_matrix[start][end]=1
        self.adjacency_matrix[end] [start]=1

    def removeEdge(self, start, end):

        self.adjacency_matrix[start,end],self.adjacency_matrix[end, start]=0,0

    def printMatrix(self):

        print("Matrix")
        print("Number of vertices %d" %(len(self.vertices)))
        for i in self.vertices:
            print "Vertex %d" %i
            for j in self.vertices:
                print(self.adjacency_matrix[i][j])


    def DFS(self, v):
        print(v)
        self.used.append(v)
        for i in self.vertices:
            if self.adjacency_matrix[v][i]==1 and i not in self.used:
                self.DFS(i)

def main():

    graph = GraphADT(20)

    graph.addVertex(1)
    graph.addVertex(2)
    graph.addVertex(3)
    graph.addVertex(4)
    graph.addEdge(1,2)
    graph.addEdge(1,3)
    graph.addEdge(2,4)
    graph.printMatrix()
    print("DFS Traversal from vertex 1: ")
    del graph.used[:]
    graph.DFS(1)

    graph.removeVertex(4)
    graph.printMatrix()
    print("DFS Traversal from vertex 1: ")

    del graph.used[:]
    graph.DFS(1)


if __name__ == "__main__":
    main()
