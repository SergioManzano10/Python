def read_fasta(thefastcat):
    '''
    >>> read_fasta('thefastcat.fasta')
    ('fast_cat', 'THEFASTCAT')
    
    '''
    with open ('thefastcat.fasta') as seq_file:
        sequence = seq_file.read().splitlines()
        part1 = sequence[0][1:]
        part2 = sequence[1][0:]
        
        return part1, part2 # Esto devuelve una tupla directamente