def ways(total, k):
    # Write your code here
    memo={}
    def rec(total,k):
        if total <= 0:
            return 0
        if k == 1 or total == 1:
            return 1
        sum=0
        if (total,k) in memo:
            return memo[(total,k)]
        for i in range(1,k+1):
            sum+=rec(total-i,i)
        memo[(total,k)]=sum
        return sum
    return rec(total,k)
    
