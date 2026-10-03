from utilidades import complemento_dna

CEBADOR_ARN = "UUU"  # Representación simbólica del cebador de ARN


def replicar_dna(cadena_lider_53: str, tamano_fragmento: int = 30):
    print("\n--- 1. REPLICACIÓN DEL ADN ---")

    print("[Helicasa]: Desenrollando y separando la doble hélice de ADN...")
    hebra_a = cadena_lider_53               # hebra parental A (la secuencia de entrada)
    hebra_b = complemento_dna(hebra_a)      # hebra parental B (complementaria)
    print(f"  - Hebra parental A: {hebra_a[:50]}...")
    print(f"  - Hebra parental B: {hebra_b[:50]}...")

    cadena_lider = complemento_dna(hebra_b)
    print(f"  - Cadena Líder (copia continua de B): {cadena_lider[:50]}...")

    print("\n[Primasa & ADN Polimerasa]: Sintetizando cadena rezagada por fragmentos...")
    fragmentos_okazaki = []
    for i in range(0, len(hebra_a), tamano_fragmento):
        sub_molde = hebra_a[i:i + tamano_fragmento]
        fragmentos_okazaki.append(CEBADOR_ARN + complemento_dna(sub_molde))

    print(f"  - Se generaron {len(fragmentos_okazaki)} fragmentos de Okazaki.")
    print(f"  - Muestra del 1er fragmento (cebador RNA + ADN): {fragmentos_okazaki[0]}")

    print("[ADN Ligasa]: Eliminando cebadores y sellando los fragmentos de Okazaki...")
    cadena_rezagada = "".join(f[len(CEBADOR_ARN):] for f in fragmentos_okazaki)

    return cadena_lider, cadena_rezagada