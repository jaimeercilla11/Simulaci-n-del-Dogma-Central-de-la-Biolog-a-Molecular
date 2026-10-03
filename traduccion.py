from utilidades import TABLA_ARN


def traduccion(arnm: str) -> str:

    print("\n--- 3. TRADUCCIÓN ---")
    print("[Ribosoma]: Buscando codón de inicio (AUG)...")

    posicion_inicio = arnm.find('AUG')
    if posicion_inicio == -1:
        print("ADVERTENCIA: No se encontró codón de inicio (AUG).")
        return ""

    print(f"  - Codón AUG detectado en el nucleótido {posicion_inicio}.")

    proteina = []
    parada_encontrada = False

    for i in range(posicion_inicio, len(arnm) - 2, 3):
        codon = arnm[i:i + 3]
        aminoacido = TABLA_ARN.get(codon, '?')

        if aminoacido == 'STOP':
            print(f"[Ribosoma]: Codón de parada ({codon}) alcanzado. Finalizando traducción.")
            parada_encontrada = True
            break

        proteina.append(aminoacido)

    if not parada_encontrada:
        print("ADVERTENCIA: la secuencia terminó sin codón de parada (proteína incompleta).")

    secuencia_proteina = "".join(proteina)
    print(f"  - Cadena peptídica/Proteína final ({len(secuencia_proteina)} aminoácidos): {secuencia_proteina[:40]}...")
    return secuencia_proteina