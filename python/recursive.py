import io
def factorial_loop (n):
    if n == 0:
        return 1
    return factorial_loop(n-1)*n

print(factorial_loop(101))
