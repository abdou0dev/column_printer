columns = [
    ['1', '22', '333', '4444'], # col[0]
    ['10', '200', '3000'],      # col[1]
    ['7', '88', '999', '1'],
    ['abb', 'Adxs']     
]

max_len = max(len(col) for col in columns) # Registering length for columns calculation.
# Registering the biggest length for every inner list for columns separation.
max_just = [0] * len(columns)
for i in range(len(columns)):
    for j in range(len(columns[i])):
        if max_just[i] < len(columns[i][j]):
            max_just[i] = len(columns[i][j])

for row in range(max_len):
    for col in range(len(columns)):
        if row < len(columns[col]):
            print(columns[col][row].ljust(max_just[col] + 2), end='')
        else:
            print(' '.ljust(max_just[col] + 2), end='')
    print()
