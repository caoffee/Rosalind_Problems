with open ('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_revp.txt') as file:
    lines = file.read().strip().splitlines()
    dna = "".join(lines[1:])

def rev_comp(seq):
    comp = {'A': 'T',
        'T': 'A',
        'C': 'G',
        'G': 'C'
            }
    rev_seq = seq[::-1]
    result = []

    for base in rev_seq:
        result.append(comp[base])

    return "".join(result)

for i in range(len(dna)):
    for l in range(4, 13):
        if i + l <= len(dna):
            sub = dna[i:i+l]
            if sub == rev_comp(sub):
                print(i+1, l)


    
