import os

from utilidades import cargar_secuencia_fasta, complemento_dna
from replicacion_dna import replicar_dna
from transcripcion import transcripcion
from traduccion import traduccion

# Ruta relativa al propio script, para que funcione desde cualquier directorio
RUTA_DATASET = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                            "ncbi_dataset", "data", "gene.fna")

SECUENCIA_EJEMPLO = ("ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTT"
                     "AATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAG")


def ejecutar_simulacion():
    print("==========================================================")
    print(" SIMULACIÓN DEL DOGMA CENTRAL DE LA BIOLOGÍA MOLECULAR")
    print("==========================================================")

    try:
        adn_secuencia = cargar_secuencia_fasta(RUTA_DATASET)
        print(f"Secuencia del gen lacZ cargada con éxito ({len(adn_secuencia)} bp).")
    except FileNotFoundError:
        print("\n!!! ATENCIÓN: no se encontró el dataset real (ncbi_dataset/data/gene.fna).")
        print("!!! Se usará una secuencia de EJEMPLO corta: el resultado NO es el del gen lacZ completo.\n")
        adn_secuencia = SECUENCIA_EJEMPLO

    lider, rezagada = replicar_dna(adn_secuencia)

    arn_m = transcripcion(complemento_dna(lider))

    proteina = traduccion(arn_m)

    print("\n----------------------------------------------------------")
    print(" Flujo genético simulado correctamente.")
    print("----------------------------------------------------------")


if __name__ == "__main__":
    ejecutar_simulacion()