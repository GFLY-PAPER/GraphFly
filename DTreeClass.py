class DTree():
    def __init__(self,vertexId):
        self.vertexid=vertexId
        self.child=[]
        self.parent=None
        self.isHyperVertex=False
        self.hyPerVertexStore=[]
        self.redundantPath=[]  #存储的是指向该顶点的冗余源顶点
        self.HyperNum=None

    def insertChild(self,newNode):
        self.child.append(newNode)

    def setParent(self,parentNode):
        self.parent=parentNode

    def getChild(self):
        return self.child

    def getparent(self):
        return self.parent

    def getVertexId(self):
        return self.vertexid

    def setHyperVertex(self,isHyper):
        self.isHyperVertex=isHyper

    def addHyperVertex(self,vertexNumber):
        self.hyPerVertexStore.append(vertexNumber)

    def getHyPerVertexStore(self):
        return self.hyPerVertexStore

    def setHyperNum(self, Num):
        self.HyperNum=Num

    def getHyperNum(self):
        self.HyperNum
    
    def getIsHyperVertex(self):
        return self.isHyperVertex