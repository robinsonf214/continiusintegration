def calculateFibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        previous = 0
        current = 1
        for i in range(2, n + 1):
            temp = current
            current = previous + current
            previous = temp
        return current

# Ejemplo de uso
n = 10

resultado = calculateFibonacci(n)
print("El resultado de Fibonacci para n =", n, "es:", resultado)

