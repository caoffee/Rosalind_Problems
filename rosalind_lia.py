with open ('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_lia.txt') as file:
    k, N = map(int, file.read().strip().split())
    
import math

n = 2 ** k
p =0.25
prob = 0

for i in range(N, n + 1):
    prob += math.comb(n, i) * (p ** i) * ((1-p) ** (n-i))
    
print(prob)
