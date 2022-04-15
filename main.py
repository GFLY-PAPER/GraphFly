

import copy
from DTreeClass import *
from flowRelated import *


def checkTag(sourceTag,destTag):
    sourceTagStr=''.join(str(h) for h in sourceTag)
    destTagStr=''.join(str(h) for h in destTag)
    if sourceTagStr==destTagStr:
        return True
    if sourceTagStr.find(destTagStr)==0:   
        partTreeId=len(destTag)  
        # print("sourceTaG",sourceTagStr)
        # print("destTag",destTagStr)
        partVertexId=sourceTag[partTreeId]
        partVertexParentId=eachVertexLowerDTreePointer[partVertexId].getparent().getVertexId()
        return j>=partVertexParentId   
    else:
        return False


with open(r'Cit-HepPh.txt','r',encoding='utf-8') as file:
    content_list = file.readlines()
    dictVertex={}  
    vertexId=0
    vertexEdge={}  
    upperTrees={}
    lowerTrees={}
    eachVertexUpperDTreePointer={}  
    eachVertexLowerDTreePointer={}  
    eachVertexNumInFlow={}
    eachVertexLowerDTreeTag={}
    for x in content_list:
        if x.find("#") ==-1 :
            x=x.split('\n',1)[0]
            x=x.split('\t',1)
            if x[0]==x[1]:
                continue
            src=-1
            dst=-1
            if dictVertex.get(x[0]) == None:
                vertexId=vertexId+1
                dictVertex[x[0]]=vertexId
                src=vertexId
                vertexEdge[src]=[]
            else:
                src=dictVertex[x[0]]

            if dictVertex.get(x[1]) == None:
                vertexId=vertexId+1
                dictVertex[x[1]]=vertexId
                dst=vertexId
                vertexEdge[dst]=[]
            else:
                dst=dictVertex[x[1]]

            sourceX=int(src)
            destX=int(dst)
            if sourceX > destX:
                temp=src
                src=dst
                dst=temp
            
            if int(src) ==int(dst):
                print("dage,error")
                exit(0)
            vertexEdge[src].append(dst)

              

    
    for key in vertexEdge.keys():
        vertexEdge[key]=list(set(vertexEdge[key]))
        vertexEdge[key].sort()

    # vertexEdge={1:[2,3,4],2:[5],3:[5],4:[5,6],5:[8],6:[7],7:[8],8:[],9:[],10:[],11:[]}  #测试数据
    # vertexId=10

    for i in range(vertexId,0,-1):
        lowerFirst=0
        upperFirst=0
        upperEdgeNum=0
        lowerEdgeNum=0
        # print(i,vertexEdge[i])
        for j in vertexEdge[i]:
            
            # if i>j:
            #     print(i,j)
            #     print("error")
            #     exit(0)
            if i < j:       
                lowerEdgeNum = lowerEdgeNum +1
                if lowerFirst==0:
                    lowerFirst=lowerFirst+1
                    newLowerTree=DTree(i)
                    getparentChild=eachVertexLowerDTreePointer[j].getChild()
                    if len(getparentChild)==0:
                        eachVertexLowerDTreeTag[i]=eachVertexLowerDTreeTag[j]
                        # print("I am here",eachVertexLowerDTreeTag[i])
                    else:
                        eachVertexLowerDTreeTag[i]=copy.deepcopy(eachVertexLowerDTreeTag[j])
                        for eachTag in eachVertexLowerDTreeTag[i] :
                            # print(eachTag)
                            eachTag.append(i)
                        # print("I am here in :",i,eachVertexLowerDTreeTag[i])

                    eachVertexLowerDTreePointer[j].insertChild(newLowerTree)
                    eachVertexLowerDTreePointer[i]=newLowerTree
                    eachVertexLowerDTreePointer[i].setParent(eachVertexLowerDTreePointer[j])
                    
                else:
                    # print("SourceTag",eachVertexLowerDTreeTag[i])
                    # print("DestTag",eachVertexLowerDTreeTag[j])
                    isSame=checkTag(eachVertexLowerDTreeTag[i][0],eachVertexLowerDTreeTag[j][0])
                    if not isSame:
                        eachVertexLowerDTreePointer[i].setHyperVertex(True)
                        eachVertexLowerDTreePointer[i].addHyperVertex(j)
                        eachVertexLowerDTreePointer[j].setHyperNum(i)
                            # else: 
                            #     if eachVertexLowerDTreePointer[j].getIsHyperVertex()==True:
                            #         hyperVertexNum=eachVertexLowerDTreePointer[j].getHyperNum()
                            #         hyperTagIsSame=checkTag(eachSourceTag,eachVertexLowerDTreeTag[hyperVertexNum])
                            #         if hyperTagIsSame:
                                        
                                    # getparentChild=eachVertexLowerDTreePointer[j].getChild()
                                    # if len(getparentChild)==0:
                                    #     tmpTag=copy.deepcopy(eachVertexLowerDTreeTag[j])
                                    #     eachVertexLowerDTreeTag[i].append(tmpTag)
                                    #     print("This is temp Tag",i,eachVertexLowerDTreeTag[i])
                                        
                                #     else:
                                #         tmpTag=copy.deepcopy(eachVertexLowerDTreeTag[j])
                                #         for eachTag in tmpTag:
                                #             eachTag.append(i)
                                #         eachVertexLowerDTreeTag[i].append(tmpTag)
                                #     print("I am hyper",i,eachVertexLowerDTreeTag[i])
                            
                                # print("sourceTag",eachSourceTag)
                                # print("destTag",eachDestTag)
                                # print("I am part treeid:",eachSourceTag[partTreeId])
                                # print("parentId",partVertexParentId)
                                # print("destId",j)



                    
            # if i > j:        
            #     upperEdgeNum=upperEdgeNum+1
            #     if upperFirst==0:
            #         upperFirst=upperFirst+1
            #         eachVertexUpperDTreePointer[i][1].append(vertexEdge[i][j])

        if lowerEdgeNum==0:  
           newLowerTree=DTree(i)  
           treeId=len(lowerTrees)+1
           lowerTrees[treeId]=newLowerTree
           eachVertexLowerDTreePointer[i]=newLowerTree
           eachVertexLowerDTreeTag[i]=[[i]]

        # if upperEdgeNum==0:  
        #    newLowerTree=[[i],[]]  
        #    treeId=len(lowerTrees)+1
        #    upperTrees[treeId]=newLowerTree
        #    eachVertexUpperDTreePointer[i]=newLowerTree

            

                 
    test1=[]
    test1.append([])
    test2=test1[0]
    test1[0].append([1,2,3,4,5])
    # print("Now, i want to check tag..............")
    # for key in eachVertexLowerDTreeTag.keys():
    #     print(key,":  ",eachVertexLowerDTreeTag[key],"hyperVertex:",eachVertexLowerDTreePointer[key].getHyPerVertexStore())

    # print("The length of tree,",len(lowerTrees),vertexId)
    # print(lowerTrees[1].getVertexId())
    # outPutTree(lowerTrees[1])
    flowNum=0
    Flowset={}
    for key in lowerTrees.keys():
        child=lowerTrees[key].getChild()
        eachVertexNumInFlow[lowerTrees[key].getVertexId()]=flowNum
        if len(child)==0:
            Flowset[flowNum]=[lowerTrees[key].getVertexId()]
        for childx in child:
            vertexset=[]
            SetOutput=outPutTree(childx,vertexset)
            Flowset[flowNum]=SetOutput
            for eachV in SetOutput:
                # print(eachV)
                eachVertexNumInFlow[eachV]=flowNum

            flowNum=flowNum+1
            # if flowNum==3665:
            #     print("error,please confirm here")
            #     exit(0)    
            

    for i in range(1,vertexId+1):
        if eachVertexLowerDTreePointer[i].getIsHyperVertex()==True:
            allHyperVertex=eachVertexLowerDTreePointer[i].getHyPerVertexStore()
            for eachHyper in allHyperVertex:
                # print(i,"I am here",len(eachVertexNumInFlow),vertexId)
                if eachVertexNumInFlow[i]!= eachVertexNumInFlow[eachHyper]:
                    minFlow=min([eachVertexNumInFlow[i],eachVertexNumInFlow[eachHyper]])
                    maxFlow=max([eachVertexNumInFlow[i],eachVertexNumInFlow[eachHyper]])
                    if len(Flowset[minFlow])<500:
                        for flowVertex in Flowset[maxFlow]: 
                            Flowset[minFlow].append(flowVertex)
                            eachVertexNumInFlow[flowVertex]=minFlow
                        Flowset[maxFlow]=[]



    allEdgeNum=0
    hit=0
    for x in Flowset[0]:
        allEdgeNum=allEdgeNum+len(vertexEdge[x])
        for y in vertexEdge[x]:
            if eachVertexNumInFlow[y]==0:
                hit=hit+1

    # print("AllEdge:",allEdgeNum," hits:",hit)

    
    f=open('iniGraph.txt','w')
    for i in range(1,vertexId+1):
        for x in vertexEdge[i]:
            printStr=str(i)+'\t'+str(x)+'\n'
            f.write(printStr)
    f.close()

    flowLast={}
    AllVertexTag=[]
    for eachset in Flowset.keys():
        outputStr=""
        flowLast[eachset]=[]
        for eachvertex in Flowset[eachset]:

            if eachvertex not in flowLast[eachset] and (eachvertex not in AllVertexTag):
                flowLast[eachset].append(eachvertex)
                AllVertexTag.append(eachvertex)
             
            if eachVertexLowerDTreePointer[eachvertex].getparent()!=None:
                theParent=eachVertexLowerDTreePointer[eachvertex].getparent().getVertexId()
                if theParent not in flowLast[eachset] and (theParent not in AllVertexTag):
                    index=flowLast[eachset].index(eachvertex)
                    insertIndex=index+1
                    flowLast[eachset].insert(insertIndex,theParent)
                    AllVertexTag.append(theParent)

    # for eachset in Flowset.keys():
    #     if len(flowLast[eachset])!= len(Flowset[eachset]):

    #         print("Oh, you can't",len(flowLast[eachset]),len(Flowset[eachset]))
    #         exit(0)


    vertexAllNum=0
    testVertex=[]
    f=open(r'flowInfo.txt','w')
    for key in flowLast.keys():
        printStr=""
        vertexAllNum=vertexAllNum+len(flowLast[key])
        for x in flowLast[key]:
            printStr=printStr+"\t"+str(x)
            testVertex.append(x)
        printStr=printStr+"\n"
        f.write(printStr)
    f.close()

    # print("all vertex Num:",len(testVertex),len(list(set(testVertex))),vertexAllNum)

    # print(Flowset)


      
