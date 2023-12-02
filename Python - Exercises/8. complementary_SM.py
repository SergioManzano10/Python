# Create a program (complementary.py) with3 functions:
# * compl(): returns the complementary DNA strand (AACTAAG --> TTGATTC).
# * reverse(): returns the same strand, but reversed (AACTAAG --> GAATCAA).
# * reverse_compl(): returns the reverse complementary strand (AACTAAG --> CTTAGTT)

# that given a DNA sequence prints the complementary, the reverse and the reverse complementary sequences
# complementary.pyComplementary and reverse sequences


dna = input("Enter your DNA sequence: ")

#Reverse function

def reverse(dna):
    """"
    >>> reverse('AACTAAG')
    'GAATCAA'

    """
    reversed_dna = dna[::-1]
    return reversed_dna

print(reverse(dna))

#Complementary function

complementary_bases = {"A": "T", "T": "A", "C": "G", "G": "C"}

def compl(dna):
    """"
    >>> compl('AACTAAG')
    'TTGATTC'

    """
    out = [] 
    for base in dna:
        complementaria = complementary_bases[base] 
        acumula = out.append(complementaria)
        sequence_complementary = "".join(out)
    return sequence_complementary

print(compl(dna))

#Reverse + Complementary function

def rev_compl(dna):
    """"
    >>> rev_compl('AACTAAG')
    'CTTAGTT'

    """
    out = [] 
    for base in dna:
        complementaria = complementary_bases[base] 
        acumula = out.append(complementaria)
        sequence_complementary = "".join(out)
        complementary_and_reverse = sequence_complementary[::-1]
    return complementary_and_reverse

print(rev_compl(dna))
       