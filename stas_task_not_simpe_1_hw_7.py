def function_1(square_length):
    p = square_length * 4
    d = 2 ** 0.5 * square_length
    s = square_length ** 2
    return (p, d, s)


print(function_1(5))
