import random   # Import the random library to generate random numbers

# ============================================
# MATRIX DECLARATION
# ============================================
A = []  # Matrix A (will be filled with random numbers)
B = []  # Matrix B (will be filled with random numbers)
C = []  # Matrix C (will contain the sum of A and B)
D = []  # Matrix D (will contain the subtraction of A and B)
E = []  # Matrix E (will contain the multiplication of A x B)
temp = 0  # Temporary variable for calculations (used in multiplication and sorting)

# ============================================
# DEFINE MATRIX SIZE
# ============================================
# The size (n) will be random between 3 and 6 (i.e., matrix 3x3, 4x4, 5x5 or 6x6)
n = random.randint(3, 6)
print("The matrix size is", n)

# ============================================
# FILL MATRICES A and B
# ============================================
# In this loop we create the rows for each matrix
for i in range(n):
    A.append([])  # Create a new empty row in A
    B.append([])  # Create a new empty row in B
    C.append([])  # Create a new empty row in C
    D.append([])  # Create a new empty row in D
    E.append([])  # Create a new empty row in E

    # Traverse each column of the row
    for j in range(n):
        A[i].append(random.randint(1, 10))  # Generate a random number for A
        B[i].append(random.randint(1, 10))  # Generate a random number for B
        C[i].append(A[i][j] + B[i][j])      # Element-wise addition → C = A + B
        D[i].append(A[i][j] - B[i][j])      # Element-wise subtraction → D = A - B

# ============================================
# DISPLAY MATRICES A, B, C and D
# ============================================
print("Matrix A")
for row in A:
    print(row)

print("Matrix B")
for row in B:
    print(row)

print("Matrix C (A+B)")
for row in C:
    print(row)

print("Matrix D (A-B)")
for row in D:
    print(row)

# ============================================
# MATRIX MULTIPLICATION → E = A x B
# ============================================
# Formula: E[i][j] = SUM( A[i][k] * B[k][j] ) for k=0 to n-1
for i in range(n):  # Traverse rows of A
    for j in range(n):  # Traverse columns of B
        for k in range(n):  # Traverse each element to multiply and sum
            temp += A[i][k] * B[k][j]
        E[i].append(temp)  # Save result in E
        temp = 0           # Reset variable for next calculation

print("Matrix E (A x B)")
for row in E:
    print(row)

# ============================================
# SORT MATRIX E (Bubble sort)
# ============================================
# Traverse the ENTIRE matrix comparing element by element
# and swap if they are out of order (if the first is smaller than the second)
for i in range(n):
    for j in range(n):
        for k in range(n):
            for m in range(n):
                if E[i][j] < E[k][m]:  # If current element is smaller, swap them
                    temp = E[i][j]
                    E[i][j] = E[k][m]
                    E[k][m] = temp

print("Matrix E Sorted (from largest to smallest)")
for row in E:
    print(row)
