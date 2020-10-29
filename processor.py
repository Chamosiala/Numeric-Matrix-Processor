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


running = True
while running:
    matrixA = []
    matrixB = []
    matrixC = []

    choice = input("1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices\n4. Transpose matrix\n0. "
                   "Exit\nYour choice: ")

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

    elif choice == '0':
        running = False
