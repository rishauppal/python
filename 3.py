matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12],
]
new=[]
for i in range(4):
    new_row=[]
    for matrix_row in matrix:
        new_row.append(matrix_row[i])
    new.append(new_row)
print(new
