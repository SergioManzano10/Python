# Write a code that prints, for each character of a sequence, a message telling if the character contains G, C or another type of base.

seq = "CGATCGA"
print(seq)

for base in seq: #para cada elemento de seq
    if "C" in base: #si en el elemento que toque es una C, que ponga esta base es una C
        print("this base is a C")
    elif "G" in base:
        print("this base is a G")
    else: print ("this base is different from C or G")