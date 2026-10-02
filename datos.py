

TABLA_CODONES = {
    'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
    'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
    'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
    'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
    'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
    'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
    'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
    'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
    'TAC':'Y', 'TAT':'Y', 'TAA':'STOP', 'TAG':'STOP',
    'TGC':'C', 'TGT':'C', 'TGA':'STOP', 'TGG':'W',
}


def cargar_secuencia_fasta(ruta_archivo: str) -> str:
    """Lee un archivo FASTA/FNA ignorando los encabezados (líneas que empiezan por '>')."""
    secuencia = []
    with open(ruta_archivo, 'r') as f:
        for linea in f:
            linea_limpia = linea.strip()
            if not linea_limpia.startswith('>'):
                secuencia.append(linea_limpia.upper())
    return "".join(secuencia)


def complemento_dna(cadena_dna: str) -> str:
    """Genera la cadena complementaria de ADN según A<->T y C<->G."""
    tabla = str.maketrans('ATCG', 'TAGC')
    return cadena_dna.translate(tabla)