def read_fasta(filename):
    sequences = {}
    label = None
    with open(filename) as file:
        for line in file:
            if line.startswith(">"):
                label = line[1:].strip()
                sequences[label] = []
            else:
                sequences[label].append(line.strip())
    result = {}
    for label, parts in sequences.items():
        result[label] = "".join(parts)
    return result

#compare base by position
def compare_base(s1, s2):
    transitions = 0
    transversions = 0
    purine = frozenset({'A', 'G'})
    pyrimidine = frozenset({'C', 'T'})
    for base1, base2 in zip(s1, s2):
        if base1 != base2:
            if base1 in purine and base2 in purine:
                transitions += 1
            elif base1 in pyrimidine and base2 in pyrimidine:
                transitions += 1
            else:
                transversions += 1
    ratio = round(transitions / transversions, 11)
    return ratio

data = read_fasta('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_tran.txt')
s1, s2 = data.values()
print(compare_base(s1, s2))








