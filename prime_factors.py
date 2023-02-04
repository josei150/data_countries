def factors(value):
    factors_values = []
    num_primes = [2, 3, 5, 7]
    num_limit = value//2 + 1

    if value > 10000000:
        num_limit = 10000000

    #almacenar primos menores que el número ingresado
    for i in range(11, num_limit):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            num_primes.append(i)
    
    print(num_primes)
    print(len(num_primes))


    while value != 1:
        
        for i in num_primes:
            if value % i == 0:
                factors_values.append(i)
                value /= i
                break

    return factors_values

def factores(startnum):
    prime_factors = []
    factor = 2 # Begin with a Divisor of 2
    while startnum > 1:
        if startnum % factor == 0:
            prime_factors.append(factor)
            startnum /= factor # divide the startnum by the factor
        else: # If the divisor is not a factor increase it by 1
            factor += 1
    return prime_factors

if __name__ == "__main__":
    print(factores(104743))
    #print(factors(100))