import snap
import numpy as np
import matplotlib.pyplot as plt
import math


def main():
    G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(G,OutDegV)
    dict = {}
    for item in OutDegV:
        node = item.GetVal2()
        if node in dict:
            dict[node] += 1
        else:
            dict[node] = 1
    x = []
    y = []
    for key,values in dict.items():
        if key>0 and values>0:
            x.append(math.log(key,10))
            y.append(math.log(values,10))
    z1 = np.polyfit(x,y,1)
    p1 = np.poly1d(z1)
    yvals = p1(x)
    plt.plot(x,y, '*',label='original values')
    plt.plot(x,yvals, 'r',label='polyfit values')
    plt.xlabel('x=log(Out-Grades)')
    plt.ylabel('y=log(Sum of the Nodes)')
    plt.show()

    
if __name__ == "__main__":
    main()
