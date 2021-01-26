# Print the number of balls for the largest triangle
# that could be made with n balls lying around.
# Bart Massey 2021

# The triangle calculation.
def triangle_loop(n):
    row_length = 1
    balls_used = 0
    while n > row_length:
        n = n - row_length
        balls_used = balls_used + row_length
        row_length = row_length + 1
    return balls_used

n = int(input("number of balls? "))
print(triangle(n))
