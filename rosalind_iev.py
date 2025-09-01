with open('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_iev.txt') as file:
    num = list(map(int, file.read().strip().split()))

prob = [2, 2, 2, 1.5, 1, 0]

result = 0
for n, p in zip(num, prob):
    result += n * p

print(result)
    
