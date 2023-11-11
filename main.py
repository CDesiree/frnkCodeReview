import numpy as np


def input_matrix(m, n):
    matrix = []
    print(f"\nEnter {m}x{n} matrix:")
    for i in range(m):
        row = []
        for j in range(n):
            value = float(input(f"Enter the element at row {i + 1}, column {j + 1}: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)


def define_matrix():
    m = int(input("\nEnter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    A = input_matrix(m, n)
    B = input_matrix(m, n)
    return A, B


def add_matrix(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 + matrix2
    else:
        print("Matrix dimensions must match for addition.")


def subtract_matrix(matrix1, matrix2):
    if matrix1.shape == matrix2.shape:
        return matrix1 - matrix2
    else:
        print("Matrix dimensions must match for subtraction.")


def scalar_matrix():
    m = int(input("\nEnter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    A = input_matrix(m, n)
    scalar = float(input("Enter the scalar value: "))
    return A * scalar


def multiply_matrix(matrix1, matrix2):
    if matrix1.shape[1] == matrix2.shape[0]:
        return np.dot(matrix1, matrix2)
    else:
        print("Number of columns in the first matrix must match the number of rows in the second matrix for "
              "multiplication.")


def transpose():
    m = int(input("\nEnter the number of rows: "))
    n = int(input("Enter the number of columns: "))
    A = input_matrix(m, n)
    return np.transpose(A)


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


print("\nMatrix Operations:")
print("1. Add Matrices")
print("2. Subtract Matrices")
print("3. Multiply Matrix by Scalar")
print("4. Multiply Matrices")
print("5. Transpose Matrix")
print("6. Calculate Determinant")
print("7. Calculate Matrix Inverse")
print("8. Quit")

while True:
    choice = int(input("\nEnter your choice: "))

    if choice == 69:
        print("\nBOORAT")

    if choice == 8:
        break

    if choice not in range(1, 9):
        print("Invalid choice. Please enter a valid option.\n")
        continue

    if choice == 1:
        A, B = define_matrix()
        result = add_matrix(A, B)

    if choice == 2:
        A, B = define_matrix()
        result = subtract_matrix(A, B)

    if choice == 3:
        scalar_matrix()

    if choice == 4:
        A, B = define_matrix()
        result = multiply_matrix(A, B)

    if choice == 5:
        result = transpose()

    if choice == 6:
        m = int(input("\nEnter the number of rows: "))
        n = int(input("Enter the number of columns: "))
        A = input_matrix(m, n)
        if m == n:
            result = np.linalg.det(A)
        else:
            print("Determinant can only be calculated for square matrices.")

    if choice == 7:
        m = int(input("\nEnter the number of rows: "))
        n = int(input("Enter the number of columns: "))
        A = input_matrix(m, n)
        if m == n:
            try:
                result = np.linalg.inv(A)
            except np.linalg.LinAlgError:
                print("Matrix is singular; it does not have an inverse.")

    print("\nResult:\n", result)

print("Goodbye!")
