row_col = int (input ("Enter the number of collumns and rows:"))
matrix = []
for row in range (row_col):
    matrix.append ([])
    for col in range(row_col):
        matrix[row].append (col + 1 +
row * row_col)
sum = 0
for i in range (row_col):
    sum += matrix[i] [row_col - i - 1]
print (*matrix, sep = "\n")
print (sum)