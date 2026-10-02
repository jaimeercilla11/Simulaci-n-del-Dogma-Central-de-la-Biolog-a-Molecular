from datos import cargar_secuencia_fasta, complemento_dna
from replicacion_dna import replicar_dna
from transcripcion import transcripcion
from traduccion import traduccion

def ejecutar_simulacion():
    print("==========================================================")
    print(" SIMULACIÓN DEL DOGMA CENTRAL DE LA BIOLOGÍA MOLECULAR")
    print("==========================================================")
    
    ruta_dataset = "ncbi_dataset/data/gene.fna"
    
    # Cargar datos
    try:
        adn_secuencia = cargar_secuencia_fasta(ruta_dataset)
        print(f"Secuencia del gen lacZ cargada con éxito ({len(adn_secuencia)} bp).")
    except FileNotFoundError:
        print("Archivo gene.fna no encontrado. Ejecutando con secuencia de ejemplo corta...")
        adn_secuencia = "ATGACCATGATTACGGATTCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAG"

    # Paso 1: Replicación
    lider, rezagada = replicar_dna(adn_secuencia)
    
    # Paso 2: Transcripción (usamos la cadena complementaria como molde)
    arn_m = transcripcion(complemento_dna(lider))
    
    # Paso 3: Traducción
    proteina = traduccion(arn_m)
    
    print("\n----------------------------------------------------------")
    print(" Flujo genético simulado correctamente.")
    print("----------------------------------------------------------")

if __name__ == "__main__":
    ejecutar_simulacion()