# Convert from protein name to gene name

# * Create a function prot2gene(prot_name) to convert from protein name to gene name (CRFR1_RAT --> Crhr1). Use Biopython (ExPASy and SwissProt modules).

# * Write a script that reads all protein names in entries.txt and prints (as output) the associated gene names.

# * HINT: ExPASy.get_sprot_raw() can accept both: ids(P35353) and names (CRFR1_RAT)

from Bio import ExPASy
import Bio.SwissProt as sp

def prot2gene(proteins):
    '''
    >>> prot2gene(["PACR_BOVIN"])
    ['ADCYAP1R1']
    >>> prot2gene([""])
    []
    >>> prot2gene(["AAAAA_HUMAN"])
    []
    '''
    gene_names = []
    for protein in proteins:
        try: 
            if protein: # Verifica si la variable protein no está vacía o es diferente de None. # Si la proteína no está vacía, el bloque de código dentro del if se ejecuta. Esto evita que se procesen proteínas vacías.
                with ExPASy.get_sprot_raw(protein) as record_file:
                    records = sp.parse(record_file)
                    for record in records:
                        if record.gene_name: # Verifica si el objeto record tiene un atributo gene_name y si este atributo no está vacío o es diferente de None. # Si gene_name existe y no está vacío, el bloque de código dentro del if se ejecuta. Esto asegura que solo se procesen registros que tengan un nombre de gen.
                            split_gene_name = record.gene_name.split('Name=')[1].split(';', 1)[0].strip() # .split('Name='): Utiliza el método split para dividir la cadena en fragmentos, utilizando "Name=" como delimitador. Esto crea una lista de partes, y estamos interesados en la segunda parte de esta lista (índice 1), ya que queremos lo que sigue después de "Name=". # [1].split(';', 1): Se aplica otro split, pero esta vez usando ";" como delimitador y limitando la cantidad de divisiones a 1. Nuevamente, estamos interesados en la primera parte de esta nueva división (índice 0), ya que queremos lo que está antes del primer punto y coma. # [0]: Finalmente, accede al primer elemento de la última lista resultante después de la segunda división. Esto nos dará la parte deseada después de "Name=" y antes del primer punto y coma.
                            if split_gene_name: # Verifica si la variable split_gene_name no está vacía o es diferente de None. # Si split_gene_name no está vacío, el bloque de código dentro del if se ejecuta. Esto garantiza que solo se añadan nombres de genes no vacíos a la lista gene_names.
                                gene_names.append(split_gene_name)
        except ValueError: #El bucle de arriba lo ejecuta para todos los elementos de entries, exceptuando el valor de "AAAAA_HUMAN" que no se encuentra en SwissProt y por eso da error
            return []

    return gene_names

# To obtain the protein name from a file
with open("entries.txt") as protnames:
    proteins = protnames.read().splitlines()

# To display the results
print(prot2gene(proteins))


