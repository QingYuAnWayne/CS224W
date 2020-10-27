import snap



def main():
    network = snap.LoadEdgeList(snap.PNEANet,"/Users/qingyuan/CS224W/stackoverflow-Java.txt",0,1)
    Components = snap.TCnComV()
    snap.GetWccs(network,Components)
    print("The number of weakly connected components is %d" % Components.Len())
    MxWcc = snap.GetMxWcc(network)
    print("The number of edges is %d and the number of nodes is %d in the largest weakly connected component." 
        % (MxWcc.GetNodes(), MxWcc.GetEdges()))
    PRankH = snap.TIntFltH()
    snap.GetPageRank(network, PRankH)
    PRankH.SortByDat(False)
    num = 0
    print("IDs of the top 3 most central nodes in the network by PagePank scores. ")
    for item in PRankH:
        print(item, PRankH[item])
        num += 1
        if num == 3:
            num = 0
            break 
    NIdHubH = snap.TIntFltH()
    NIdAuthH = snap.TIntFltH()
    snap.GetHits(network, NIdHubH, NIdAuthH)
    NIdHubH.SortByDat(False)
    print("IDs of the top 3 hubs in the network by HITS scores. ")
    for item in NIdHubH:
        print(item, NIdHubH[item])
        num += 1
        if num == 3:
            num = 0
            break 
    NIdAuthH.SortByDat(False)
    print("IDs of top 3 authorities in the network by HITS scores. ")
    for item in NIdAuthH:
        print(item, NIdAuthH[item])
        num += 1
        if num == 3:
            num = 0
            break 


    

if __name__ == '__main__':
    main()
    