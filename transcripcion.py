"""
Módulo transcripcion.py
Simula la transcripción de la hebra molde de ADN a ARN mensajero (ARNm).
"""

def transcripcion(cadena_dna_molde: str) -> str:
    """
    Sintetiza ARNm a partir de la hebra molde de ADN.
    Regla de complementariedad: A->U, T->A, C->G, G->C.
    """
    print("\n--- 2. TRANSCRIPCIÓN ---")
    print("[ARN Polimerasa]: Leyendo la hebra molde de ADN...")
    
    tabla_arn = str.maketrans('ATCG', 'UAGC')
    arnm = cadena_dna_molde.translate(tabla_arn)
    
    print(f"  - ARNm Sintetizado (5'->3'): {arnm[:60]}...")
    return arnm