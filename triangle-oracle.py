# Print the number of balls for the largest triangle
# that could be made with n balls lying around.
# Bart Massey 2021

import math

# The triangle calculation.
def triangle_loop(n):
    row_length = 1
    balls_used = 0
    while n >= row_length:
        n = n - row_length
        balls_used = balls_used + row_length
        row_length = row_length + 1
    return balls_used

# The other triangle calculation.
def triangle_math(n):
        k = int(math.floor((math.sqrt(1 + 8 * n) - 1) / 2))
        return k * (k + 1) // 2

for n in range(27):
        print(n, triangle_loop(n), triangle_math(n))

for n in range(100, 601, 100):
        print(n, triangle_loop(n), triangle_math(n))
