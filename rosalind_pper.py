with open ('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_pper.txt') as file:
    n, k = map(int, file.read().split())

result = 1

for i in range(k):
    result = result * (n - i) % 1000000

print(result)
