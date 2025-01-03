import sys

t = int(input())
result = []
# for _ in range(t):
#     col, row = map(int, input().split())
#     if row == col:
#         diagonal = (col * col) - (col - 1)
#         result.append(diagonal)
#     elif row  < col:
#         diagonal = (col * col) - (col - 1)
#         if col % 2 == 0:
#             result.append(diagonal + (row - 1))
#         else:
#             result.append(diagonal - (row - 1))
#     elif row > col:
#         prompt = max(row, col)
#         diagonal = ((prompt - 1) * (prompt - 1)) + prompt
#         if row % 2 == 0:
#             result.append(diagonal + (prompt - 1))
#         else:
#             result.append(diagonal - (prompt - 1))

for _ in range(t):
    col, row = map(int, input().split())

    if row == col:
        d = (col * col) - (col - 1)
        result.append(d)
    elif col > row:
        d = (col * col) - (col - 1)
        if col % 2 == 0:
            result.append(d + (col - row))
        else:
            result.append(d - (col - row))
    else:
        d = (row * row) - (row - 1)
        if row % 2 == 0:
            result.append(d - (row - col))
        else:
            result.append(d + (row - col))

result = [str(x) for x in result]
sys.stdout.write("\n".join(result) + "\n")
