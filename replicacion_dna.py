from datos import complementaria_dna, complementaria_rna


def replicacion_dna(cadena_molde_3to5):
    print("\n--- 1. REPLICACIÓN DEL ADN ---")

    if len(cadena_molde_3to5) > 40:
        print(f"Cadena Molde (3'->5') [Muestra primeros 40 nt]: {cadena_molde_3to5[:40]}...")
    else:
        print(f"Cadena Molde (3'->5'):  {cadena_molde_3to5}")

    cadena_lider = "".join([complementaria_dna(b) for b in cadena_molde_3to5])

    if len(cadena_lider) > 40:
        print(f"Cadena Líder (5'->3') [Muestra]: {cadena_lider[:40]}...")
    else:
        print(f"Cadena Líder (5'->3'): {cadena_lider}")

    tamano_okazaki = 4
    fragmentos = []

    limite_longitud = min(20, len(cadena_molde_3to5))

    for i in range(0, limite_longitud, tamano_okazaki):
        bloque = cadena_molde_3to5[i:i + tamano_okazaki]
        cebador = "RNA_PRIMER(" + "".join([complementaria_rna(b) for b in bloque[:2]]) + ")"
        sintesis = "".join([complementaria_dna(b) for b in bloque[2:]])
        fragmentos.append(f"[{cebador} + {sintesis}]")

    print("\nSimulación de Cadena Rezagada (Fragmentos de Okazaki - Muestra inicial):")
    for idx, frag in enumerate(fragmentos, 1):
        print(f"  Fragmento Okazaki {idx}: {frag}")

    return cadena_lider