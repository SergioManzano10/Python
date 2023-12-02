# Define a function reading_frames() which takes as arguments a position (0, 1 or 2) and a DNA/RNA (str) and returns a list with the triplets that will be translated into protein.

# * reading_frames(0, 'GTGATTAA’) --> [' GTG ', ' ATT’]
# * reading_frames(1, 'GTGATTAA’) --> ['TGA’ , 'TTA’]
# * reading_frames(2, 'GTGATTAA’) --> ['GAT’, ‘TAA’]

dna = input("Enter your DNA sequence: ")

def reading_frames(position, dna): 
    """
    >>> reading_frames(0, 'GTGATTAA')
    ['GTG', 'ATT']
    >>> reading_frames(1, 'GTGATTAA')
    ['TGA', 'TTA']
    >>> reading_frames(2, 'GTGATTAA')
    ['GAT', 'TAA']

    """
    triplets = []                  
    for base in range(position, len(dna)-2, 3): 
        codon = dna[base:base + 3] 
        triplets.append(codon) 
    return triplets


print(reading_frames(0, dna)) #Parámetros para cada condición
print(reading_frames(1, dna))
print(reading_frames(2, dna))