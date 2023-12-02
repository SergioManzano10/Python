# Write a function naive_match(p, t) that returns a list with the offsets of all ocurrences of pattern p in the string t. Do not use .find(). Slide the pattern over text one by one and check for a match (this is called the Naive Match Algorithm).

p = "FAST"
t = "THEFASTCATTHEFASTRATAFASTRAT"

def naive_match(p,t): 
   """
    >>> naive_match('FAST', 'THEFASTCATTHEFASTRATAFASTRAT')
    [3, 13, 21]
    >>> naive_match('FAST', 'FAST')
    [0]
    >>> naive_match('FASTA', 'FAST')
    [] 
    
   """
   positions = []
   for i in range(len(t) - len(p) + 1):
      if t[i:i+len(p)] == p:
         positions.append(i) 
   return positions

naive_match(p,t)




