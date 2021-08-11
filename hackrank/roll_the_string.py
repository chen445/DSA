def rollTheString(s, roll):
    # Write your code here
    alp="abcdefghijklmnopqrstuvwxyz"
    arr=list(s)
    for r in range(len(roll)):
        for i in range(0,roll[r]):
            index=(alp.index(arr[i])+1)%len(alp)
            arr[i]=alp[index]
    return "".join(arr)
            