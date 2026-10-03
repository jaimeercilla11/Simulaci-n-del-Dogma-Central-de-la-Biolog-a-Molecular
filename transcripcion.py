
def transcripcion(cadena_dna_molde: str) -> str:

    print("\n--- 2. TRANSCRIPCIÓN ---")
    print("[ARN Polimerasa]: Leyendo la hebra molde de ADN...")
    
    tabla_arn = str.maketrans('ATCG', 'UAGC')
    arnm = cadena_dna_molde.translate(tabla_arn)
    
    print(f"  - ARNm Sintetizado (5'->3'): {arnm[:60]}...")
    return arnm