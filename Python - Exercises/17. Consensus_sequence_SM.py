# Write a function that returns the consensus sequence of an alignment in tm3.fa

def sequence_consensus(sequences):

    filtered_sequences = []

    with open("tm3.fa") as seq_file:
        for line in seq_file:
            if not line.startswith('>'):
                filtered_sequences.append(line.strip())


    filtered_sequences
    n = len(filtered_sequences)


    profile_matrix = {
        "A": [0]*n,
        "C": [0]*n,
        "D": [0]*n,
        "E": [0]*n,
        "F": [0]*n,
        "G": [0]*n,
        "H": [0]*n,
        "I": [0]*n,
        "K": [0]*n,
        "L": [0]*n,
        "M": [0]*n,
        "N": [0]*n,
        "P": [0]*n,
        "Q": [0]*n,
        "R": [0]*n,
        "S": [0]*n,
        "T": [0]*n,
        "V": [0]*n,
        "W": [0]*n,
        "Y": [0]*n,
    }


    for dna in filtered_sequences:
        for position, nucleotide in enumerate(dna):
            profile_matrix[nucleotide][position] += 1


    aminoacid_list = list(profile_matrix.keys())

    result = []

    for position in range(n): 
        max_count = 0
        max_nucleotide = None
        for nucleotide in aminoacid_list:
            count = profile_matrix[nucleotide][position]
            if count > max_count:
                max_count = count
                max_nucleotide = nucleotide
        result.append(max_nucleotide)

    filtered_list = [value for value in result if value is not None]

    consensus = "".join(filtered_list)
    print(consensus)
    return consensus

