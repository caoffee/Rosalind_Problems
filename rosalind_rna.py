with open ("/Users/caochuqiu/Documents/Rosalind Problems/rosalind_rna.txt") as file:
    dna = file.read().strip()

alphabet = {"A": "A",
       "C": "C",
       "G": "G",
       "T": "U"
       }

rna = ""

for letter in dna:
    rna += alphabet.get(letter)

print(rna)
