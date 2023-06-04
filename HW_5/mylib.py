def degree(A, B):
    if B == 1:
        return A
    return A * degree(A, B-1)


def sum(a, b):
    if b < 1:
        return a
    return sum(a+1, b-1)







