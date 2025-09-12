with open('/Users/caochuqiu/Documents/Rosalind Problems/rosalind_prob.txt') as file:
    dna = file.readline().strip()
    probes = list(map(float, file.readline().split()))

import math
num_A = dna.count("A")
num_C = dna.count("C")
num_G = dna.count("G")
num_T = dna.count("T")

log_probes = []
for element in probes:
    gc_probe = element / 2
    at_probe = (1 - element) / 2
    prob = gc_probe ** (num_G + num_C) * at_probe ** (num_A + num_T)
    log_probe = math.log10(prob)
    log_probes.append(round(log_probe, 3))

print(" ".join(map(str, log_probes)))
