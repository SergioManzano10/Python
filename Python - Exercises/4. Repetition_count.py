# Given a sequence, count how many times there is repetition of the same base at two consecutive positions.

input="AACGTTCAA"

res = 0 

for i in range(len(input) - 1): 
    if input[i] == input[i + 1]: 
        res+=1

print("Hay",res,"repeticiones")