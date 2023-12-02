# Convert a string of type Ala-Phe-Gly-Ala-Gly-Phe from three letter to one letter amino acid code (AFGAGF) using a dictionary.

chain = [("ALA", "A"),("PHE", "F"),("GLY", "G"),("ALA", "A"),("GLY", "G"),("PHE", "F")]
print(chain)



letters = [] 
for i in range(len(chain)):
    letters.append(chain[i][0])

chain_joined = "-".join(letters)
print(chain_joined)



letters = [] 
for i in range(len(chain)):
    letters.append(chain[i][1])

chain_joined = "".join(letters)
print(chain_joined)