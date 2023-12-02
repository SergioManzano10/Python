# Write a function that returns a list with all the words of lenght k contained in the query.

introduced_chain = "QLNFQLMSAGQLQ"
k = 3

def kmers(introduced_chain, k):
    """
    >>> kmers("QLNFQLMSAGQLQ", 3)
    ['QLN', 'LNF', 'NFQ', 'FQL', 'QLM', 'LMS', 'MSA', 'SAG', 'AGQ', 'GQL', 'QLQ']
    >>> kmers("QLNFQLMSAGQLQ", 4)
    ['QLNF', 'LNFQ', 'NFQL', 'FQLM', 'QLMS', 'LMSA', 'MSAG', 'SAGQ', 'AGQL', 'GQLQ']
    
    """
    letters = []
    for i in range(len(introduced_chain) - k + 1):
        letters.append(introduced_chain[i:i+k])
    return(letters)
    
print(kmers(introduced_chain, k))