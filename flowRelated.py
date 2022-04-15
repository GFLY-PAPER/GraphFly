def outPutTree(DtreeObj,vertexidSet):
    vertexid=DtreeObj.getVertexId()
    vertexidSet.append(vertexid)
    # print("I am :",vertexid ,"I am following children:")
    child=DtreeObj.getChild()
    for childId in child:
        outPutTree(childId,vertexidSet)
    return vertexidSet


