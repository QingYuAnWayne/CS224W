import snap
import math


def getLocalFeatures(Node, Graph):
    dgree = Node.GetDeg()
    Neibors = []
    ei = 0
    InEdgeEgonet = 0
    for i in range(0, Node.GetDeg()):
        Neibors.append(Node.GetNbrNId(i))
    Neibors.append(Node.GetId())
    for E1 in Neibors:
        for E2 in Neibors:
            if Graph.IsEdge(E1, E2):
                ei += 1
    ei /= 2
    for N in Neibors:
        NodeI = Graph.GetNI(N)
        for i in range(0, NodeI.GetDeg()):
            if NodeI.GetNbrNId(i) not in Neibors:
                InEdgeEgonet += 1
    return dgree, ei, InEdgeEgonet


def getAllNodesLocalFeatures(Graph):
    NodeFeatureList = []
    for Node in Graph.Nodes():
        degree, ei, InEdgeEgonet = getLocalFeatures(Node, Graph)
        NodeFeatureList.append({Node.GetId(): {"degree": degree, "ei": ei, "InEdgeEgonet": InEdgeEgonet}})
    return NodeFeatureList


def getSim(Nodea, Nodeb, NodeFeatureList):
    FeatureX = NodeFeatureList[Nodea].get(Nodea)
    FeatureY = NodeFeatureList[Nodeb].get(Nodeb)
    Sim = 0.0
    t1 = FeatureX.get("degree") * FeatureY.get("degree") +FeatureX.get("ei") * FeatureY.get("ei") + FeatureX.get("InEdgeEgonet") * FeatureY.get("InEdgeEgonet")
    t2 = math.pow(FeatureX.get("degree"), 2) + math.pow(FeatureX.get("ei"), 2) + math.pow(FeatureX.get("InEdgeEgonet"), 2)
    t3 = math.pow(FeatureY.get("degree"), 2) + math.pow(FeatureY.get("ei"), 2) + math.pow(FeatureY.get("InEdgeEgonet"), 2)
    if t2 == 0 or t3 == 0:
        return 0
    else:
        Sim = t1 / (math.sqrt(t2) * math.sqrt(t3))
        return Sim


FIn = snap.TFIn("hw1-q2.graph")
Graph = snap.TUNGraph.Load(FIn)
NodeFeatureList = getAllNodesLocalFeatures(Graph)
SimList = []
for node in Graph.Nodes():
    if node.GetId() != 9:
        SimList.append({'nodeId': node.GetId(), 'Sim': getSim(9, node.GetId(), NodeFeatureList)})
for i in range(0,len(SimList)):
    for j in range(0,i):
        if SimList[i].get('Sim') > SimList[j].get('Sim'):
            temp = SimList[j]
            SimList[j] = SimList[i]
            SimList[i] = temp
for i in range(0, 5):
    print(SimList[i])
