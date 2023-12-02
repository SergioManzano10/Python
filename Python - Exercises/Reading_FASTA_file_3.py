filename = input("Introduce the filename in .fasta format: ")
filename

def read_fasta(filename):
    '''
    >>> read_fasta('thefastcat.fasta')
    {'fast_cat': 'THEFASTCAT'}
    >>> read_fasta('fastcats.fasta')
    {'FAST_CAT': 'THE----FASTCAT', 'FAT_RAT': 'THE----FA-TRAT', 'VERYFAST_CAT': 'THEVERYFASTCAT', 'LAST_CAT': '---LASTFA-TCAT'}

    '''
    with open (filename) as archive:
        sequences = archive.read().splitlines()

    all_sequences = []
    for element in sequences:
        if element.startswith(">"):
            all_sequences.append(element[1:])
        else:
            all_sequences.append(element)
    
    dictionary = {all_sequences[i]: all_sequences[i + 1] for i in range(0, len(all_sequences), 2)}

    return dictionary

print(read_fasta(filename))