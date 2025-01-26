# Open the file
file = open("/Users/caochuqiu/Downloads/rosalind_dna.txt", "r")
string = file.read().strip().replace("\n", "") #Clean up the DNA sequence
file.close() #always close the file after reading

#Function to count nucleotides
def count_dna(string):
    count1 = string.count("A")
    count2 = string.count("C")
    count3 = string.count("G")
    count4 = string.count("T")
    return count1, count2, count3, count4

if __name__ =="__main__":
    # Count nucleotides
    count_acgt = count_dna(string)
    print(" ".join(map(str, count_acgt))) # Print counts formatted as space-separated values
