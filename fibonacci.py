def fibonacci_dinamico(n, memo = {}):
    if n == 0 or n == 1:
        return 1

    print("entré 2:", n)

    try:
        print("entré 1:", n)

        return memo[n]
    except KeyError:
        print("entré")
        resultado = fibonacci_dinamico(n - 1, memo) + fibonacci_dinamico(n - 2, memo)
        print(resultado)
        memo[n] = resultado

        return resultado

if __name__ == '__main__':
    
    n = int(input('Escoge un numero: '))
    resultado = fibonacci_dinamico(n)
    print(resultado)