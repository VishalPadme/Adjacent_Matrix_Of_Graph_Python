#Module
class graph:
    def __init__(self,size):
        self.adj=[[0 for i in range(size)]for j in range(size)]
        self.size=size
    def addEdge(self,v1,v2):
        if (v1==v2):
            print(v1," and ",v2," are Same Vertex")
        self.adj[v1][v2]=1
        self.adj[v2][v1] = 1
    def removeEdge(self,v1,v2):
        if (self.isEdgeContain(v1,v2)):
            self.adj[v1][v2] = 0
            self.adj[v2][v1] = 0
            print(' Edge  Between ', v1, " and ", v2, "Has Been Removed")
        else:
            print('No edge Between ',v1," and ",v2)
    def isEdgeContain(self,v1,v2):
        if(self.adj[v1][v2]==0):
            return False
        elif(self.adj[v1][v2]==1):
            return True
    def display(self):
        print("__|",end="")
        for i in range(self.size):
            if i < 10:
                print(i, end=" |")
            else:
                print(i, end="|")


        print("")
        for i in range(self.size):
            if i<10:
                print(i, end=" |")
            else:
                print(i, end="|")
            for j in range(self.size):
                print(self.adj[i][j],end="  ")
            print("")

    def isPath(self, v1, v2):
        l = [v1]
        for v in l:
            for i in range(self.size):
                if ((self.adj[v][i] == 1 ) and (i not in l)):
                    l.append(i)
        if v2 in l:
            return True
        else:
            return False

#driver
v=int(input("Enter The Number of Vertices: "))
g=graph(v)
print("MENU:\n\t[1] Add Edge\n\t[2] Remove Edge\n\t[3] Check Whether there is Edge Or not\n\t[4] Number Of Vertices\n\t[5] Display a")
ch=int(input("Enter Your Choise: "))
while(ch<7):
    try:

        if (ch == 1):
            v1 = int(input("Enter First Vertex : "))
            v2 = int(input("Enter Second Vertex: "))
            g.addEdge(v1,v2)
            print(' Edge Has Been Added Between ', v1, " and ", v2)
        elif (ch==2):
            v1 = int(input("Enter First Vertex : "))
            v2 = int(input("Enter Second Vertex: "))
            g.removeEdge(v1, v2)
        elif (ch==3):
            v1 = int(input("Enter First Vertex : "))
            v2 = int(input("Enter Second Vertex: "))
            if(g.isEdgeContain(v1,v2)):
                print('There is a edge Between ', v1, " and ", v2)
            else:
                print('There is No edge Between ', v1, " and ", v2)
        elif (ch==4):
            print("Number Of The Vertices In Graph := ",g.size)
        elif (ch==5):
            g.display()
        elif (ch==6):
            v1 = int(input("Enter Source Vertex : "))
            v2 = int(input("Enter Destination Vertex: "))
            if(g.isPath(v1,v2)):
                print("There is a path between ",v1,"  & ",v2)
            else:
                print("There is No path between ", v1, "  & ", v2)

        ch = int(input("Enter Your Next Choise: "))
    except IndexError:
        print("!![Please Enter Valid Vertices]!!")
