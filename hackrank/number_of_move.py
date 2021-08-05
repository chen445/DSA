def minMoves(n, startRow, startCol, endRow, endCol):
    # Write your code here
    queue=[[startRow,startCol]]
    visited=[[startRow,startCol]]
    next_queue=[]
    count=1
    while len(queue) !=0:
        for node in queue:
            for e in getNei(node[0],node[1],n):
                if e[0]==endRow and e[1]==endCol:
                    return count
                if e not in visited:
                    next_queue.append(e)
                    visited.append(e)
        queue=next_queue
        next_queue=[]
        count+=1
    return -1

def getNei(row,col,n):
    arr=[[row+2,col+1],[row+2,col-1],[row-2,col+1],[row-2,col-1],[row+1,col+2],[row-1,col+2],[row-1,col-2],[row+1,col-2]]
    new_arr=[]
    for e in arr:
        if e[0]>=0 and e[0]<n and e[1]>=0 and e[1]<n:
            new_arr.append(e)
    return new_arr
    