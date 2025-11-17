def read_fasta(filename):
    sequences = []
    seq = ""

    with open(filename) as file:
        for line in file:
            line = line.strip()
            if line.startswith('>'):
                if seq:
                    sequences.append(seq)
                    seq = ""
            else:
                seq += line
        sequences.append(seq)

    return sequences

s, t = read_fasta('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_sseq.txt')

def find_motif(s, t):
    i = 0 #pointer for t
    result = []
    for index in range(len(s)):
        if s[index] == t[i]:
            result.append(index+1)
            i += 1
            if i == len(t):
                break
    return result

result = find_motif(s, t)
print(*result)




