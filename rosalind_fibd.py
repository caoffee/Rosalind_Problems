with open('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_fibd.txt') as file:
    n, m = map(int, file.read().strip().split())

def mort_fib(n, m):
    ages = [1] + [0] * (m-1)
    for month in range(2, n+1):
        newborns = sum(ages[1:])
        ages = [newborns] + ages[:-1]
    return sum(ages)

print(mort_fib(n, m))
