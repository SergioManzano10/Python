# Given two sequences with the same length:
# * Count the number of matched bases at the same position.
# * Print a string that has ‘*’ at the matched positions and spaces at the unmatched positions.


chain1 = "AAAAAAAA"
chain2 = "AGCTATAA"

result = 0
alignment =""
for dna1, dna2 in zip(chain1, chain2):
    if dna1 == dna2:
        result+=1
    else:
        result+=0
        
for dna1, dna2 in zip(chain1, chain2):
    if dna1 == dna2:
        alignment +="*"
    else:
        alignment+=" "

print("There are",result, "matches")

print(chain1)
print(chain2)
print(alignment.strip())