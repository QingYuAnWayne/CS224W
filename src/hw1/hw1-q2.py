import snap
import math
import numpy as np
import matplotlib.pyplot as plt


def getLocalFeatures(Node, Graph):
    dgree = float(Node.GetDeg())
    Neibors = getNeibors(Node)
    ei = 0.0
    InEdgeEgonet = 0.0
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


def getNeibors(Node):
    Neibors = []
    for i in range(0, Node.GetDeg()):
        Neibors.append(Node.GetNbrNId(i))
    return Neibors


def getAllNodesLocalFeatures(Graph, k):
    NodeFeatureList = []
    for Node in Graph.Nodes():
        vector = []
        degree, ei, InEdgeEgonet = getLocalFeatures(Node, Graph)
        vector.extend([Node.GetId(), degree, ei, InEdgeEgonet])
        NodeFeatureList.append(vector)
    for i in range(0, k):
        for Node in Graph.Nodes():
            CurNodeId = Node.GetId()
            Neibors = getNeibors(Node)
            sum_list = []
            mean_list = []
            for j in range(1, len(NodeFeatureList[CurNodeId])):
                sum_list.append(0)
                mean_list.append(0)
            for NodeId in Neibors:
                for j in range(1, len(NodeFeatureList[CurNodeId])):
                    sum_list[j - 1] += NodeFeatureList[NodeId][j]
            if len(Neibors) != 0:
                NodeFeatureList[CurNodeId].extend(sum_list)
                mean_list = sum_list[:]
                for j in range(0, len(mean_list)):
                    mean_list[j] = mean_list[j] / len(Neibors)
                NodeFeatureList[CurNodeId].extend(mean_list)
            else:
                NodeFeatureList[CurNodeId].extend(mean_list)
                NodeFeatureList[CurNodeId].extend(mean_list)
    return NodeFeatureList


def getSim(Nodea, Nodeb, NodeFeatureList):
    FeatureX = NodeFeatureList[Nodea]
    FeatureY = NodeFeatureList[Nodeb]
    Sim = 0.0
    t1 = 0
    t2 = 0
    t3 = 0
    for i in range(1, len(NodeFeatureList[0])):
        t1 += FeatureX[i] * FeatureY[i]
        t2 += math.pow(FeatureX[i], 2)
        t3 += math.pow(FeatureY[i], 2)
    if t2 == 0 or t3 == 0:
        return 0
    else:
        Sim = t1 / (math.sqrt(t2) * math.sqrt(t3))
        return Sim


k = 2
FIn = snap.TFIn("hw1-q2.graph")
Graph = snap.TUNGraph.Load(FIn)
NodeFeatureList = getAllNodesLocalFeatures(Graph, k)
SimList = []
for node in Graph.Nodes():
    if node.GetId() != 9:
        SimList.append([node.GetId(), getSim(9, node.GetId(), NodeFeatureList)])

# here we sort by sim
def takeSecond(elem):
    return elem[1]


SimList.sort(key=takeSecond, reverse=True)
i = 0
for j in range(0, 5):
    print(SimList[i])
    while SimList[i + 1][1] == SimList[i][1]:
        # print(SimList[i + 1])
        i += 1
    i += 1

data = []
for item in SimList:
    data.append(item[1])

plt.hist(data, bins=20, range=(0, 1),rwidth=0.8)
plt.xlabel("cosine similarity with node 9")
plt.ylabel("the number of nodes")
plt.show()