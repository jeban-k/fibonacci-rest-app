memo = {0:0, 1:1}
def fib(n):
    list1=[]
    if not n in memo:
        memo[n] = fib(n-1) + fib(n-2)
        list1.append(memo[n])
    return list1
print fib(20000)
