def parse_fasta(filename):
    with open(filename) as file:
        s = file.readline().strip()
        t = file.readline().strip()
    return s, t

def scsp(s, t):
    m, n = len(s), len(t)

    #build DP table
    dp = [[0] * (n+1) for _ in range(m+1)]

    for i in range(m+1):
        dp[i][0] = i
    for j in range(n+1):
        dp[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s[i-1] == t[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1

    #traceback
    result = []
    i, j = m, n
    while i > 0 and j > 0:
        if s[i-1] == t[j-1]:
            result.append(s[i-1])
            i -= 1
            j -= 1
        elif dp[i-1][j] < dp[i][j-1]: #going up, emit s[i-1]
            result.append(s[i-1])
            i -= 1
        else: #going left, emit t[j-1]
            result.append(t[j-1])
            j -= 1

    while i > 0:
        result.append(s[i - 1])
        i -= 1
    while j > 0:
        result.append(t[j - 1])
        j -= 1

    return ''.join(reversed(result))

s, t = parse_fasta('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_scsp.txt')
print(scsp(s, t))


