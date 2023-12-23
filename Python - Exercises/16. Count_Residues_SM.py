### Write a function count_residue(fasta_file, residue) reads a file in .fasta format (fastcats.fasta) and counts how many times one specific residue (base or amino acid) appears in total through all sequences.

cat_sequences = []
with open("fastcats.fasta") as sequence_file:
    for line in sequence_file:
        if not line.startswith('>'):
            cat_sequences.append(line.strip())

out_letters = input("Introduce one letter: ")


def count_residue(cat_sequences, out_letters):
   
    out_letters = out_letters.upper()
    total_count = 0
    for sequence in cat_sequences:
        for letter in sequence:
            total_count += letter.count(out_letters)
        # print(total_count) # Así me diría el número de veces que se repite esa letra en cada palabra
    print(total_count) 

    return(total_count)

count_residue(cat_sequences, out_letters)