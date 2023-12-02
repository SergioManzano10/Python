# Write a new function count_ov() that returns the number of motifs (including overlaps). Test it!

dna = input("Enter your DNA sequence: ")
motif = 'ATAT'
def count_ov(dna, motif):
    """
    >>> 'GATATAT'.count('ATAT')
    1
    >>> count_ov('GATATAT', 'ATAT')
    2
    >>> count_ov('GATATATATATGCATATATACTT', 'ATAT')
    6
    >>> count_ov('GAT', 'ATAT')
    0
    >>> count_ov('GAT', '') 
    0

    """
    count = 0
    for base in range(len(dna) - len(motif) + 1): 
        if dna[base:base + len(motif)] == motif: 
            count += 1

    return count

print(count_ov(dna,motif)) # Hay algo mal porque este test no lo pasa (linea 13), cuenta 4 motivos y debería contar 0
