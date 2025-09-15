with open ('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_lexv.txt') as file:
    data = file.read().strip().splitlines()
    alphabet = data[0].split()
    n = int(data[1])

def generate(current, alphabet, n, output):
    if current:
        output.write(current + "\n")

    if len(current) < n:
        for letter in alphabet:
            generate(current + letter, alphabet, n, output)

with open("output.txt", "w") as f:
    generate("", alphabet, n, f)    
