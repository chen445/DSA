# Tool List A milling machine in a manufacturing facility has a tool change system. The tool changer holds n tools and some ...

def toolchanger(tools, startIndex, target):
    # Write your code here
    i=j=startIndex
    move=0
    for _ in range(len(tools)):
        if target==tools[i] or target==tools[j]:
            return move
        i=(i+1)%len(tools)
        j=(j-1)%len(tools)
        move+=1
    return -1
    