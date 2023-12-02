
#dna_rna_proteindna_rna_protein.py

#Think of a possible algorithm to detect the type of sequence that the user enters (expect only DNA, RNA or protein). Write it!
#The code should show a message with the text "DNA" or "RNA", or "Protein",accordingly.

seq=input('Enter your sequence: ')
seq=seq.upper()

if all(base in 'ACG' for base in seq):
    print('Could be either RNA, DNA or protein')
elif all(base in 'ACUG' for base in seq): 
    print('RNA')
elif all(base in 'ACTG' for base in seq): 
    print('DNA')
elif all(base in 'ACDEFGHIKLMNPQRSTVWY' for base in seq): 
    print('Protein')
else: 
    print('Your sequence is not RNA, DNA or protein')

