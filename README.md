# Práctica 1: Simulación del Dogma Central de la Biología Molecular

**Asignatura:** Bioinformática (ULPGC)  
**Autor:** Jaime Ercilla Martín  

---

## Descripción del Proyecto
Este simulador en Python modela el flujo integrado de la información genética desde el ADN hasta la síntesis de una proteína funcional, cumpliendo con los tres procesos clave del dogma central:
1. **Replicación del ADN:** Formación de la cadena líder continua (5'->3') y la cadena rezagada discontinua (fragmentos de Okazaki con cebadores de RNA).
2. **Transcripción:** Obtención del ARNm a partir de la hebra molde de ADN.
3. **Traducción:** Lectura en tripletes (codones) a partir del codón de inicio (AUG) hasta el codón STOP.

## Datos Utilizados
Se ha utilizado la secuencia genómica real del gen **lacZ** (*Escherichia coli*), obtenida de las bases de datos de NCBI (`ncbi_dataset/data/gene.fna`), correspondiente a una secuencia de 3075 nucleótidos.

## Ejecución
Para ejecutar el simulador principal:
\`\`\`bash
python main.py
\`\`\`