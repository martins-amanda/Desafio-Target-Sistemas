def is_fibonacci(n):
    a, b = 0, 1
    while a <= n:
        if a == n:
            return True
        a, b = b, a + b
    return False


num = int(input("Informe um valor: "))

if is_fibonacci(num):
    print(f"O número {num} pertence a sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence a sequência de Fibonacci.")