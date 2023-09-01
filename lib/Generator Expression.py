# Generate a sequence of squares using a generator expression
squares = (x * x for x in range(1, 6))
for square in squares:
    print(square)
