def spiral_traversal(matrix):
    result = []
    if not matrix:
        return result
top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1
     while top <= bottom and left <= right:
        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1
        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1
        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1
    return result
 rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))
 print("Enter matrix elements row by row:")
matrix = []
for _ in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)
 print("Spiral Traversal:", spiral_traversal(matrix))
