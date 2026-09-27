import os

# 1. Diccionario para el código genético (Traducción)
GENETIC_CODE = {
    'AUG': 'Met (Inicio)', 'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',
    'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu', 'AUU': 'Ile',
    'AUC': 'Ile', 'AUA': 'Ile', 'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val',
    'GUG': 'Val', 'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro', 'ACU': 'Thr',
    'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr', 'GCU': 'Ala', 'GCC': 'Ala',
    'GCA': 'Ala', 'GCG': 'Ala', 'UAU': 'Tyr', 'UAC': 'Tyr', 'CAU': 'His',
    'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln', 'AAU': 'Asn', 'AAC': 'Asn',
    'AAA': 'Lys', 'AAG': 'Lys', 'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu',
    'GAG': 'Glu', 'UGU': 'Cys', 'UGC': 'Cys', 'UGG': 'Trp', 'CGU': 'Arg',
    'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGU': 'Ser', 'AGC': 'Ser',
    'AGA': 'Arg', 'AGG': 'Arg', 'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly',
    'GGG': 'Gly', 'UAA': 'STOP', 'UAG': 'STOP', 'UGA': 'STOP'
}


def complementaria_dna(base):
    pairs = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return pairs.get(base.upper(), 'N')


def complementaria_rna(base):
    pairs = {'A': 'U', 'T': 'A', 'C': 'G', 'G': 'C'}
    return pairs.get(base.upper(), 'N')


def cargar_secuencia_fasta(ruta_archivo):
    """
    Lee un archivo FASTA (.fna) ignorando la cabecera que empieza por '>'
    y devuelve la secuencia de ADN completa en mayúsculas.
    """
    if not os.path.exists(ruta_archivo):
        return None

    secuencia = []
    with open(ruta_archivo, 'r') as f:
        for linea in f:
            if not linea.startswith('>'):
                secuencia.append(linea.strip())
    return "".join(secuencia).upper()