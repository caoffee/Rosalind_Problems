def read_fasta(filename):
    sequences = []                      # will store each DNA string
    with open(filename) as f:
        seq = ""                        # temporary variable for one sequence
        for line in f:
            line = line.strip()          # remove whitespace/newlines
            if line.startswith(">"):     # if line is a header
                if seq != "":            # if we already collected a sequence
                    sequences.append(seq)
                    seq = ""             # reset for the next one
            else:
                seq += line              # add this line to the current sequence
        sequences.append(seq)            # add the final sequence
    return sequences                     # return the list (important!)


sequences = read_fasta('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_lcsm.txt')
shortest = min(sequences, key=len)

def all_substrings(s):
    n = len(s)
    for length in range(n, 0, -1):   # longest → shortest
        for start in range(n - length + 1):
            yield s[start:start+length]

def find_motif(sequences):
    shortest = min(sequences, key=len)
    for sub in all_substrings(shortest):
        if all(sub in seq for seq in sequences):
            return sub  # return first (longest) one


motif = find_motif(sequences)
print(motif)

