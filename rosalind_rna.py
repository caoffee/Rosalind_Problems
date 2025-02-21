# Open the file
file = open("/Users/caochuqiu/Desktop/Rosalind Problems/rosalind_rna.txt", "r")
string = file.read().strip().replace("\n", "") #Clean up the DNA sequence
file.close() #always close the file after reading

#Function to turn T into U
def transcribe(string):
    return string.replace("T", "U")
    
if __name__ =="__main__":
    print(transcribe(string))
