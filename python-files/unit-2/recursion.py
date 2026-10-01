def factorial(n):
    """Recursive factorial with base case."""
    if n <= 1:
        return 1
    return n * factorial(n - 1)

print(f"factorial(5) = {factorial(5)}")
print(f"factorial(0) = {factorial(0)}")

def factorial_traced(n, depth=0):
    """Factorial with trace showing recursion depth."""
    indent = "  " * depth
    print(f"{indent}factorial({n}) called")
    
    if n <= 1:
        print(f"{indent}--> base case, return 1")
        return 1
    
    result = n * factorial_traced(n - 1, depth + 1)
    print(f"{indent}--> return {result}")
    return result

factorial_traced(4)

def countdown(n):
    """Countdown recursively."""
    print(n)
    if n > 0:
        countdown(n - 1)

countdown(3)

def factorial_iterative(n):
    """Factorial using iteration instead of recursion."""
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

print(f"Iterative factorial(5) = {factorial_iterative(5)}")
