def addition():
    global matrixA, matrixB, matrixC
    for row in range(rowA):
        matrixC.append([])
        for col in range(colA):
            matrixC[row].append(str(matrixA[row][col] + matrixB[row][col]) + ' ')
        print(''.join(matrixC[row]))


def multiplication(row, col):
    global matrixA, matrixB, rowA, rowB, colA, colB
    result = 0
    _rowB = 0
    _colA = 0

    while _colA < colA and _rowB < rowB:
        result += matrixA[row][_colA] * matrixB[_rowB][col]
        _colA += 1
        _rowB += 1
    return str(result)


def matrix_multiplication(rows, cols):
    result_matrix = []
    for row in range(rows):
        result_matrix.append([])
        for col in range(cols):
            result_matrix[row].append(multiplication(row, col) + ' ')
        print(''.join(result_matrix[row]))


def transpose(rows, cols, type):
    global matrixA
    matrix = []
    if type == "main":
        for row in range(rows):
            matrix.append([])
            for col in range(cols):
                matrix[row].append(str(matrixA[col][row]) + ' ')
            print(''.join(matrix[row]))
    elif type == "side":
        j = cols - 1
        for row in range(rows):
            matrix.append([])
            i = rows - 1
            for col in range(cols):
                matrix[row].append(str(matrixA[i][j]) + ' ')
                i -= 1
            j -= 1
            print(''.join(matrix[row]))
    elif type == "vertical":
        for row in range(rows):
            matrix.append([])
            j = cols - 1
            for col in range(cols):
                matrix[row].append(str(matrixA[row][j]) + ' ')
                j -= 1
            print(''.join(matrix[row]))
    elif type == "horizontal":
        i = rows - 1
        for row in range(rows):
            matrix.append([])
            for col in range(cols):
                matrix[row].append(str(matrixA[i][col]) + ' ')
            i -= 1
            print(''.join(matrix[row]))


def copy_matrix(M):
    rows = len(M)
    cols = len(M[0])

    MC = []
    for i in range(rows):
        MC.append([])
        for j in range(cols):
            MC[i].append(0.0)

    for i in range(rows):
        for j in range(cols):
            MC[i][j] = M[i][j]

    return MC


def determinant(M, total=0):
    indices = list(range(len(M)))

    if len(M) == 2 and len(M[0]) == 2:
        return M[0][0] * M[1][1] - M[0][1] * M[1][0]
    elif len(M) == 1:
        return M[0][0]


    for fc in indices:
        Ms = copy_matrix(M)
        Ms = Ms[1:]
        height = len(Ms)

        for i in range(height):
            Ms[i] = Ms[i][0:fc] + Ms[i][fc + 1:]

        sign = (-1) ** (fc % 2)
        sub_det = determinant(Ms)
        total += sign * M[0][fc] * sub_det

    return total



running = True
while running:
    matrixA = []
    matrixB = []
    matrixC = []

    choice = input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n"
                   "5. Calculate a determinant\n0. Exit\nYour choice: ")

    if choice == '1':
        numbers = input("Enter size of the first matrix: ").split()
        rowA = int(numbers[0])
        colA = int(numbers[1])
        print("Enter first matrix: ")
        for i in range(rowA):
            matrixA.append([])
            numbers = input().split()
            for j in range(colA):
                matrixA[i].append(float(numbers[j]))

        numbers = input("Enter size of the second matrix: ").split()
        rowB = int(numbers[0])
        colB = int(numbers[1])
        print("Enter second matrix: ")
        for i in range(rowB):
            matrixB.append([])
            numbers = input().split()
            for j in range(colB):
                matrixB[i].append(float(numbers[j]))

        if rowB == rowA and colB == colA:
            print("The result is: ")
            addition()
            print()
        else:
            print("The operation cannot be performed.")

    elif choice == '2':
        numbers = input("Enter size of matrix: ").split()
        rowA = int(numbers[0])
        colA = int(numbers[1])

        for i in range(rowA):
            matrixA.append([])
            numbers = input().split()
            for j in range(colA):
                matrixA[i].append(float(numbers[j]))

        constant = float(input("Enter constant: "))
        print("The result is: ")
        for i in range(rowA):
            matrixC.append([])
            for j in range(colA):
                matrixC[i].append(str(matrixA[i][j] * constant) + ' ')
            print(''.join(matrixC[i]))
        print()

    elif choice == '3':
        numbers = input("Enter size of the first matrix: ").split()
        rowA = int(numbers[0])
        colA = int(numbers[1])
        print("Enter first matrix: ")
        for i in range(rowA):
            matrixA.append([])
            numbers = input().split()
            for j in range(colA):
                matrixA[i].append(float(numbers[j]))

        numbers = input("Enter size of the second matrix: ").split()
        rowB = int(numbers[0])
        colB = int(numbers[1])
        print("Enter second matrix: ")
        for i in range(rowB):
            matrixB.append([])
            numbers = input().split()
            for j in range(colB):
                matrixB[i].append(float(numbers[j]))

        if colA == rowB:
            print("The result is:")
            matrix_multiplication(rowA, colB)
            print()
        else:
            print("This operation cannot be performed.")

    elif choice == '4':
        print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
        choice = input("Your choice: ")
        numbers = input("Enter matrix size: ").split()
        rowA = int(numbers[0])
        colA = int(numbers[1])
        print("Enter matrix: ")
        for i in range(rowA):
            matrixA.append([])
            numbers = input().split()
            for j in range(colA):
                matrixA[i].append(float(numbers[j]))

        if choice == '1':
            print("The result is: ")
            transpose(rowA, colA, "main")
            print()
        elif choice == '2':
            print("The result is: ")
            transpose(rowA, colA, "side")
            print()
        elif choice == '3':
            print("The result is: ")
            transpose(rowA, colA, "vertical")
            print()
        elif choice == '4':
            print("The result is: ")
            transpose(rowA, colA, "horizontal")
            print()

    elif choice == '5':
        numbers = input("Enter matrix size: ").split()
        rowA = int(numbers[0])
        colA = int(numbers[1])
        print("Enter matrix: ")
        for i in range(rowA):
            matrixA.append([])
            numbers = input().split()
            for j in range(colA):
                matrixA[i].append(float(numbers[j]))

        print(f"The result is:\n{determinant(matrixA)}\n")

    elif choice == '0':
        running = False
