with open('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_lgis.txt') as file:
    n = int(file.readline().strip())
    perm = list(map(int, file.readline().split()))

def longest_subsequence(seq, increasing=True):
    dp = [1] * n
    prev = [-1] * n

    for i in range(n):
        for j in range(i):
            if (increasing and perm[j] < perm[i]) or (not increasing and seq[j] > seq[i]):
                if dp[j] + 1 > dp[i]:
                    dp[i] = dp[j] + 1
                    prev[i] = j
    #find end of longest subsequence
    max_index = dp.index(max(dp))

    #reconstruct subsequence
    subseq = []
    while max_index != -1:
        subseq.append(seq[max_index])
        max_index = prev[max_index]
    return subseq[::-1]

# --- compute LIS and LDS ---
lis = longest_subsequence(perm, increasing=True)
lds = longest_subsequence(perm, increasing=False)

print(*lis) #* is the unpacking operator
print(*lds)
