import random   # Importamos la librería random para generar números aleatorios

# ============================================
# DECLARACIÓN DE MATRICES
# ============================================
A = []  # Matriz A (se llenará con números aleatorios)
B = []  # Matriz B (se llenará con números aleatorios)
C = []  # Matriz C (contendrá la suma de A y B)
D = []  # Matriz D (contendrá la resta de A y B)
E = []  # Matriz E (contendrá la multiplicación de A x B)
auxiliar = 0  # Variable de apoyo para cálculos (se usa en multiplicación y ordenamiento)

# ============================================
# DEFINIR EL TAMAÑO DE LA MATRIZ
# ============================================
# El tamaño (n) será aleatorio entre 3 y 6 (es decir, matriz 3x3, 4x4, 5x5 o 6x6)
n = random.randint(3,6)
print("El tamaño de la matriz es", n)

# ============================================
# LLENAR LAS MATRICES A y B
# ============================================
# En este bucle se crean las filas de cada matriz
for i in range(n):
  A.append([])  # Crea una nueva fila vacía en A
  B.append([])  # Crea una nueva fila vacía en B
  C.append([])  # Crea una nueva fila vacía en C
  D.append([])  # Crea una nueva fila vacía en D
  E.append([])  # Crea una nueva fila vacía en E

  # Se recorre cada columna de la fila
  for j in range(n):
      A[i].append(random.randint(1,10))  # Genera un número aleatorio para A
      B[i].append(random.randint(1,10))  # Genera un número aleatorio para B
      C[i].append(A[i][j] + B[i][j])     # Suma elemento a elemento → C = A + B
      D[i].append(A[i][j] - B[i][j])     # Resta elemento a elemento → D = A - B

# ============================================
# MOSTRAR MATRICES A, B, C y D
# ============================================
print("Matriz A")
for i in A:
  print(i)

print("Matriz B")
for i in B:
  print(i)

print("Matriz C (A+B)")
for i in C:
  print(i)

print("Matriz D (A-B)")
for i in D:
  print(i)

# ============================================
# MULTIPLICACIÓN DE MATRICES → E = A x B
# ============================================
# Fórmula: E[i][j] = SUMA( A[i][k] * B[k][j] ) para k=0 hasta n-1
for i in range(n):  # Recorre filas de A
  for j in range(n):  # Recorre columnas de B
    for k in range(n):  # Recorre cada elemento para multiplicar y sumar
      auxiliar += A[i][k] * B[k][j]
    E[i].append(auxiliar)  # Guarda el resultado en E
    auxiliar = 0           # Reinicia la variable para el siguiente cálculo

print("Matriz E (A x B)")
for i in E:
  print(i)

# ============================================
# ORDENAR MATRIZ E (Burbuja)
# ============================================
# Se recorre TODA la matriz comparando elemento por elemento
# y se intercambian si están en desorden (si el primero es menor al segundo)
for i in range(n):
  for j in range(n):
    for k in range(n):
      for m in range(n):
        if E[i][j] < E[k][m]:  # Si el elemento actual es menor, los intercambiamos
           auxiliar = E[i][j]
           E[i][j] = E[k][m]
           E[k][m] = auxiliar

print("Matriz E Ordenada (de mayor a menor)")
for i in E:
  print(i)
