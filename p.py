def fibonacci_recursive(n):
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

num_terms = 100

if num_terms <= 0:
    print("not a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(num_terms):
        print(fibonacci_recursive(i))