#The file 'brca1_cds.dna’ contains the coding sequence of BRCA1 (each line corresponds to a coding exon).
# We would like to get: A list with the GC content of each of the exons

with open ("brca1_cds.dna") as cds_dna:
    for sequences in cds_dna:
        total_bases = len(sequences)
        c_content=sequences.count("c") 
        g_content=sequences.count("g")
        print(sequences.upper(), c_content, g_content, total_bases)
        GC_content = ((c_content + g_content)/total_bases)*100
        print("The GC content for this sequence is",GC_content, "\n")
        