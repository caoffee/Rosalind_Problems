def parse_fasta(filename):
    sequences = {}
    with open(filename) as file:
        header = ""
        seq = ""
        for line in file:
            line = line.strip()
            if line.startswith(">"):
                if seq != "":
                    sequences[header] = seq
                header = line[1:]
                seq = ""
            else:
                seq += line
            sequences[header] = seq
        return sequences

def gc_content(dna):
    g = dna.count("G")
    c = dna.count("C")
    return (g+c) / len(dna) * 100

data = parse_fasta('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_gc.txt')
max_id = ""
max_gc = 0

for seq_id in data:
    gc = gc_content(data[seq_id])
    if gc > max_gc:
        max_gc = gc
        max_id = seq_id

print(max_id)
print(f"{max_gc:.6f}")