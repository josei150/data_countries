def prime(number):
    """
    Given a number n, determine what the nth prime is.
    """
    #Basic prime numbers 
    num_primes = [2, 3, 5, 7]
    numbers = []

    if number == 0:
        raise ValueError("there is no zeroth prime")
    
    #list of numbers in range
    for i in range(11, 105000):
        #Debugging numbers that are divisible by known prime numbers
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0:
            numbers.append(i)

    count = 0
    #searching prime numbers
    while len(num_primes) < number:
        for j in numbers:
            if j % num_primes[count] == 0:
                numbers.remove(j)
        num_primes.append(numbers.pop(0))
        count += 1
    
    return num_primes[number - 1]

if __name__ == "__main__":
    print(prime(1))