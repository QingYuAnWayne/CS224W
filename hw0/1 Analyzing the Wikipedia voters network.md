## 1 Analyzing the Wikipedia voters network

1. The number of nodes in the network

   ```python
   G = snap.LoadEdgeListStr(snap.PNGraph, "Wiki-Vote.txt", 0, 1)
   print("Number of Nodes: %d" % G.GetNodes())
   ```

7115

2.

```python
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    num = 0
    for EI in G.Edges():
        if EI.GetSrcNId() == EI.GetDstNId():
            num += 1
    print(num)
```

0

3.

```python
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    num = 0
    edgenum = 0
    for EI in G.Edges():
        if EI.GetSrcNId() != EI.GetDstNId():
            num += 1
        edgenum += 1
    print(num)
    print(edgenum)
```

103689

4.

```python
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    num = 0
    for EI in G.Edges():
        if EI.GetSrcNId() != EI.GetDstNId():
            num += 1
            if G.IsEdge(EI.GetDstNId(),EI.GetSrcNId()):
                G.DelEdge(EI.GetDstNId(),EI.GetSrcNId())
    print(num)
```

100762

5.

```python
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    num = 0
    for EI in G.Edges():
            if G.IsEdge(EI.GetDstNId(),EI.GetSrcNId()) and G.IsEdge(EI.GetSrcNId(),EI.GetDstNId()):
                G.DelEdge(EI.GetDstNId(),EI.GetSrcNId())
                G.DelEdge(EI.GetSrcNId(),EI.GetDstNId())
                num += 1
    print(num)
```

2889

6.

```python
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    InDegV = snap.TIntPrV()
    snap.GetNodeInDegV(G,InDegV)
    num = 0
    for item in InDegV:
        if item.GetVal2() == 0:
            num += 1
    print(num)
```

8.

```python
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    InDegV = snap.TIntPrV()
    snap.GetNodeInDegV(G,InDegV)
    num = 0
    outgoing_num = 0
    for item in InDegV:
        if item.GetVal2() == 0:
            num += 1
        if item.GetVal2() > 10:
            outgoing_num += 1
    print(num)
    print(outgoing_num)
```

7,9

```python
G = snap.LoadEdgeList(snap.PNGraph, "wiki-Vote.txt", 0, 1)
    OutDegV = snap.TIntPrV()
    snap.GetNodeOutDegV(G,OutDegV)
    num = 0
    outgoing_num = 0
    for item in OutDegV:
        if item.GetVal2() == 0:
                num += 1
        if item.GetVal2() > 10:
                outgoing_num += 1
    print(num)
    print(outgoing_num)
```



# 2

1.

<img src="https://raw.githubusercontent.com/QingYuAnWayne/PicStorage/master/20201027092938.png?token=ANS26RQCFWROJFOERVNHRKC7S54EC" style="zoom:50%;" />

```python
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
    plt.scatter(x, y, s=10, marker='.')
    plt.xlabel('x=log(Out-Grades)')
    plt.ylabel('y=log(Sum of the Nodes)')
    plt.show()

    
if __name__ == "__main__":
    main()
```

2.

<img src="https://raw.githubusercontent.com/QingYuAnWayne/PicStorage/master/20201027103122.png?token=ANS26RWRAVX4LIKNQ6MSJR27S6DLS" style="zoom:50%;" />

```python
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
```

