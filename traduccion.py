"""
Módulo traduccion.py
Simula la traducción del ARNm a proteína en el ribosoma.
"""
from datos import TABLA_CODONES

def traduccion(arnm: str) -> str:
    """
    Busca el codón de inicio (AUG) y traduce los tripletes a aminoácidos
    hasta llegar a un codón STOP (UAA, UAG, UGA).
    """
    print("\n--- 3. TRADUCCIÓN ---")
    print("[Ribosoma]: Buscando codón de inicio (AUG)...")
    
    # Convertimos temporalmente U por T para consultar fácilmente la tabla de datos
    arnm_dna_format = arnm.replace('U', 'T')
    
    posicion_inicio = arnm_dna_format.find('ATG')
    if posicion_inicio == -1:
        print("ADVERTENCIA: No se encontró codón de inicio (AUG).")
        return ""
    
    print(f"  - Codón AUG detectado en el nucleótido {posicion_inicio}.")
    
    proteina = []
    # Lectura en marcos de lectura de 3 en 3
    for i in range(posicion_inicio, len(arnm_dna_format) - 2, 3):
        codon = arnm_dna_format[i:i+3]
        aminoacido = TABLA_CODONES.get(codon, '?')
        
        if aminoacido == 'STOP':
            print(f"[Ribosoma]: Codón de parada ({codon}) alcanzado. Finalizando traducción.")
            break
            
        proteina.append(aminoacido)
    
    secuencia_proteina = "".join(proteina)
    print(f"  - Cadena peptídica/Proteína final ({len(secuencia_proteina)} aminoácidos): {secuencia_proteina[:40]}...")
    return secuencia_proteina