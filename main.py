import numpy as np


def input_matrix(m, n):
    matrix = []
    print(f"Enter {m}x{n} matrix:")
    for i in range(m):
        row = []
        for j in range(n):
            value = float(input(f"Enter the element at row {i + 1}, column {j + 1}: "))
            row.append(value)
        matrix.append(row)
    return np.array(matrix)


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))
    while True:
        print("\nMatrix Operations:")
        print("1. Add Matrices")
        print("2. Subtract Matrices")
        print("3. Multiply Matrix by Scalar")
        print("4. Multiply Matrices")
        print("5. Transpose Matrix")
        print("6. Calculate Determinant")
        print("7. Calculate Matrix Inverse")
        print("8. Quit")

        choice = int(input("Enter your choice: "))

        if choice == 8:
            break

        if choice not in range(1, 9):
            print("Invalid choice. Please enter a valid option.")
            continue

        if choice in [1, 2, 4]:
            m = int(input("Enter the number of rows: "))
            n = int(input("Enter the number of columns: "))
            A = input_matrix(m, n)
            B = input_matrix(m, n)
        elif choice == 3:
            m = int(input("Enter the number of rows: "))
            n = int(input("Enter the number of columns: "))
            A = input_matrix(m, n)
            scalar = float(input("Enter the scalar value: "))
        elif choice in [5, 6, 7]:
            m = int(input("Enter the size of the square matrix (e.g., 2 for 2x2, 3 for 3x3, etc.): "))
            A = input_matrix(m, m)

            if choice == 1:
                if A.shape == B.shape:
                    result = A + B
            else:
                print("Matrix dimensions must match for addition.")
                continue
        elif choice == 2:
            if A.shape == B.shape:
                result = A - B
            else:
                print("Matrix dimensions must match for subtraction.")
                continue
        elif choice == 3:
            result = A * scalar
        elif choice == 4:
            if A.shape[1] == B.shape[0]:
                result = np.dot(A, B)
            else:
                print("Number of columns in the first matrix must match the number of rows in the second matrix for "
                      "multiplication.")
                continue
        elif choice == 5:
            result = np.transpose(A)
        elif choice == 6:
            if m == n:
                result = np.linalg.det(A)
            else:
                print("Determinant can only be calculated for square matrices.")
                continue
        elif choice == 7:
            if m == n:
                try:
                    result = np.linalg.inv(A)
                except np.linalg.LinAlgError:
                    print("Matrix is singular; it does not have an inverse.")
                    continue
            else:
                print("Matrix inverse can only be calculated for square matrices.")
                continue

        print("\nResult:")
        print_matrix(result)


print("Goodbye!")
