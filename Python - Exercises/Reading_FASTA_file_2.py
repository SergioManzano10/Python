with open ('thefastcat.fasta') as seq_file:
        sequence = seq_file.read().splitlines()

def print_fasta(sequence):
    '''
    >>> print_fasta(('fast_cat', 'THEFASTCAT'))
    >fast_cat
    THEFASTCAT
    >>> print_fasta(('', 'THEFASTCAT'))
    >unnamed
    THEFASTCAT
    >>> print_fasta(('', ''))
    '''

    if sequence[0] == '' and sequence[1] == '':
        return
    elif sequence[0] == '':
        return print(f">unnamed\n{sequence[1]}")
    
    return print(f">{sequence[0]}\n{sequence[1]}")

