from datos import complemento_dna

def replicar_dna(cadena_lider_53: str, tamano_fragmento: int = 30):
    """
    Simula la duplicación del ADN mostrando las enzimas involucradas:
    - Helicasa: abre la hélice.
    - Cadena Líder: síntesis continua (5' -> 3').
    - Primasa/Polimerasa: sintesis de cebadores + fragmentos de Okazaki.
    - Ligasa: unión de fragmentos en la cadena rezagada.
    """
    print("\n--- 1. REPLICACIÓN DEL ADN ---")
    
    # 1. Apertura por la Helicasa
    print("[Helicasa]: Desenrollando y separando la doble hélice de ADN...")
    cadena_molde_35 = complemento_dna(cadena_lider_53)
    
    print(f"  - Cadena Líder (5'->3'): {cadena_lider_53[:50]}...")
    print(f"  - Cadena Molde (3'->5'): {cadena_molde_35[:50]}...")
    
    # 2. Cadena Rezagada y Fragmentos de Okazaki
    print("\n[Primasa & ADN Polimerasa]: Sintetizando cadena rezagada por fragmentos...")
    fragmentos_okazaki = []
    
    for i in range(0, len(cadena_molde_35), tamano_fragmento):
        sub_molde = cadena_molde_35[i:i + tamano_fragmento]
        cebador_arn = "uuu"  # Representación simbólica del primer de ARN
        fragmento = cebador_arn + complemento_dna(sub_molde)
        fragmentos_okazaki.append(fragmento)
    
    print(f"  - Se generaron {len(fragmentos_okazaki)} fragmentos de Okazaki.")
    print(f"  - Muestra del 1er fragmento (cebador RNA + ADN): {fragmentos_okazaki[0]}")
    
    # 3. Unificación por la Ligasa
    print("[ADN Ligasa]: Eliminando cebadores y sellando los fragmentos de Okazaki...")
    cadena_rezagada_completa = complemento_dna(cadena_molde_35)
    
    return cadena_lider_53, cadena_rezagada_completa