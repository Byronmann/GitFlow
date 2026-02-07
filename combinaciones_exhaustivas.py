#BYRON RODOLFO MALDONADO PALACIOS
#202300076
#ANALISIS DE ALGORITMOS

import time  # O(1)
from pathlib import Path  # O(1)

# Constantes de configuración
X_OBJETIVO = 50           # O(1)
RUTA_DEFECTO = "datos/numeros_25.txt"  # O(1)

# ---------------------------------------------------------------------
# LECTURA DE DATOS
# ---------------------------------------------------------------------
def leer_numeros(ruta_archivo: str):
    t0 = time.perf_counter()                      # O(1)
    with open(ruta_archivo, "r", encoding="utf-8") as f:  # O(1)
        numeros = []                              # O(1) espacio inicial
        for line in f:                            # O(n) iteraciones
            numeros.append(int(line.strip()))     # O(1) amort. por iteración
    t1 = time.perf_counter()                      # O(1)
    return numeros, (t1 - t0)                     # O(1)
# Complejidad leer_numeros: Tiempo O(n), Espacio O(n) (n = #líneas)

# ---------------------------------------------------------------------
# BÚSQUEDA EXHAUSTIVA DE PARES (nC2)
# ---------------------------------------------------------------------
def buscar_pares(numeros, X):
    t0 = time.perf_counter()              # O(1)
    resultados = []                       # O(1)
    count = 0                             # O(1)
    n = len(numeros)                      # O(1)
    for i in range(n - 1):                # ~O(n) veces
        ai = numeros[i]                   # O(1)
        for j in range(i + 1, n):         # suma aritmética -> O(n^2) total
            count += 1                    # O(1)
            if ai + numeros[j] == X:      # O(1)
                resultados.append((ai, numeros[j]))  # O(1) amort.
    t1 = time.perf_counter()              # O(1)
    return resultados, count, (t1 - t0)   # O(1)
# Complejidad buscar_pares: Tiempo O(n^2), Espacio O(k) (k = #soluciones)

# ---------------------------------------------------------------------
# BÚSQUEDA EXHAUSTIVA DE TRÍOS (nC3)
# ---------------------------------------------------------------------
def buscar_trios(numeros, X):
    t0 = time.perf_counter()                      # O(1)
    resultados = []                               # O(1)
    count = 0                                     # O(1)
    n = len(numeros)                              # O(1)
    for i in range(n - 2):                        # ~O(n) veces
        ai = numeros[i]                           # O(1)
        for j in range(i + 1, n - 1):             # ~O(n) veces por i
            aj = numeros[j]                       # O(1)
            for k in range(j + 1, n):             # ~O(n) veces por (i,j)
                count += 1                        # O(1)
                if ai + aj + numeros[k] == X:     # O(1)
                    resultados.append((ai, aj, numeros[k]))  # O(1) amort.
    t1 = time.perf_counter()                      # O(1)
    return resultados, count, (t1 - t0)           # O(1)
# Complejidad buscar_trios: Tiempo O(n^3), Espacio O(k) (k = #soluciones)

# ---------------------------------------------------------------------
# UTILIDADES DE E/S
# ---------------------------------------------------------------------
def pedir_ruta():
    ruta_input = input(f"Ruta del archivo (ENTER → {RUTA_DEFECTO}): ").strip()  # O(1)
    ruta = ruta_input if ruta_input else RUTA_DEFECTO                            # O(1)
    return ruta                                                                  # O(1)
# Complejidad pedir_ruta: Tiempo O(1), Espacio O(1)

def imprimir_resultados(ruta, n, t_lectura, t2, c2, pares, t3, c3, trios):
    print("\n=== RESUMEN DE MEDICIONES ===")                                            # O(1)
    print(f"Archivo: {ruta} | n={n} | X={X_OBJETIVO}")                                  # O(1)
    print(f"Tiempo lectura archivo (s): {t_lectura:.6f}")                               # O(1)
    print(f"Tiempo 2-combinaciones (s): {t2:.6f} | #pares enumerados={c2} | #Resultados pares={len(pares)}")  # O(1)
    print(f"Tiempo 3-combinaciones (s): {t3:.6f} | #tríos enumerados={c3} | #Resultados tríos={len(trios)}")  # O(1)
    print(f"Total (s): {t_lectura + t2 + t3:.6f}")                                      # O(1)

    print("\nCombinaciones de 2 que suman X:")                                          # O(1)
    for p in pares:                                                                      # O(k2)
        print(p)                                                                         # O(1) por impresión

    print("\nCombinaciones de 3 que suman X:")                                          # O(1)
    for t in trios:                                                                      # O(k3)
        print(t)                                                                         # O(1) por impresión
# Complejidad imprimir_resultados: Tiempo O(k2 + k3), Espacio O(1)
# (k2, k3 = #resultados impresos)


# PROGRAMA PRINCIPAL

def main():
    ruta = pedir_ruta()                                 # O(1)
    if not Path(ruta).exists():                         # O(1)
        print(f"[ERROR] No existe el archivo: {ruta}")  # O(1)
        return                                          # O(1)

    numeros, t_lectura = leer_numeros(ruta)             # O(n)
    n = len(numeros)                                    # O(1)

    pares, c2, t2 = buscar_pares(numeros, X_OBJETIVO)   # O(n^2)
    trios, c3, t3 = buscar_trios(numeros, X_OBJETIVO)   # O(n^3)

    imprimir_resultados(ruta, n, t_lectura, t2, c2, pares, t3, c3, trios)  # O(k2 + k3)
# Complejidad main: Dominada por buscar_trios → Tiempo O(n^3), Espacio O(n + k2 + k3)

if __name__ == "__main__":  # O(1)
    main()                   # O(n^3) por la llamada principal
