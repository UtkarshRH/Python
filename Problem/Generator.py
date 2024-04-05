def square_generator(n):
    for i in range(n):
        yield i ** 2

# Using the generator
squares = square_generator(5)
for square in squares:
    print(square)
