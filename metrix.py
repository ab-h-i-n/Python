class Matrix:
    def __init__(self, row, col, matrix):
        self.row = row
        self.col = col
        self.matrix = matrix

    def __str__(self):
        result = "The Matrix is:\n"
        for i in range(self.row):
            for j in range(self.col):
                result += str(self.matrix[i][j]) + "\t"
            result += "\n"
        return result

    @classmethod
    def ReadMatrix(self):
        while True:
            n = int(input("Enter the number of rows: "))
            m = int(input("Enter the number of columns: "))
            if n <= 0 or m <= 0:
                print("Invalid row or column!")
            else:
                break

        M = []

        print("Enter the elements of the matrix:")
        for i in range(n):
            R = []
            for j in range(m):
                elem = int(input(f"Enter element at position ({i+1},{j+1}): "))
                R.append(elem)
            M.append(R)

        temp = self(n, m, M)
        return temp


matrix = Matrix.ReadMatrix()
print(matrix)
