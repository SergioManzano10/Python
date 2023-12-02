# Write a code that, given a string with residues, generates a list (an prints it) with all possible dipeptides that can be constructed combining the residues in the string. Repetition is possible.

input_string = "AYS"
print(input_string)

dipeptides=[]
for residue1 in input_string:
    for residue2 in input_string:
        dipeptide = residue1 + residue2
        dipeptides.append(dipeptide)

print(dipeptides)