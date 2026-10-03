# Práctica 1: Simulación del Dogma Central de la Biología Molecular

**Asignatura:** Bioinformática (ULPGC)
**Autores:** Jaime Ercilla Martín, Javier Bolivar Garcia-Izquierdo

---

## Descripción del Proyecto
Este simulador en Python modela el flujo integrado de la información genética desde el ADN hasta la síntesis de una proteína, cumpliendo con los tres procesos clave del dogma central:

1. **Replicación del ADN:** Formación de la cadena líder continua y de la cadena rezagada discontinua (fragmentos de Okazaki con cebadores de ARN). Cada cadena se copia de una hebra parental distinta, por lo que ambas son complementarias entre sí.
2. **Transcripción:** Obtención del ARNm a partir de la hebra molde de ADN.
3. **Traducción:** Lectura en tripletes (codones) a partir del codón de inicio (AUG) hasta el codón STOP, usando el código genético con codones de ARN.

## Estructura del proyecto

| Archivo | Contenido |
|---|---|
| `main.py` | Punto de entrada: carga el gen y encadena los tres procesos. |
| `replicacion_dna.py` | Replicación: helicasa, cadena líder, fragmentos de Okazaki y ligasa. |
| `transcripcion.py` | Transcripción de la hebra molde a ARNm. |
| `traduccion.py` | Traducción del ARNm a proteína. |
| `utilidades.py` | Tabla del código genético, lectura de FASTA y complementariedad del ADN. |
| `ncbi_dataset/` | Datos descargados de NCBI (secuencia del gen en `data/gene.fna`). |

## Datos Utilizados
Se ha utilizado la secuencia genómica real del gen **lacZ** (*Escherichia coli* K-12 MG1655), obtenida de la base de datos de NCBI (`ncbi_dataset/data/gene.fna`), con una longitud de 3075 nucleótidos. La proteína resultante, la β-galactosidasa, tiene 1024 aminoácidos.

Si no se encuentra `gene.fna`, el programa avisa y usa una secuencia de ejemplo corta (el resultado en ese caso no corresponde al gen completo).

## Ejecución
Para ejecutar el simulador principal, desde la carpeta del proyecto:

```bash
python main.py
```

## Simplificaciones del modelo
- El cebador de ARN es simbólico (`UUU`) y los fragmentos de Okazaki tienen un tamaño fijo de 30 nt.
- La transcripción parte directamente de la hebra molde, sin promotor ni terminador.
- No se modelan intrones ni procesamiento del ARNm (los genes de *E. coli* no los tienen).