def is_prime(N):
    number = False
    for i in range(1, N):
        if (N % i) == 0 and i != 1 and i != N:
            number = False
            break
        else:
            number = True
    return number

def print_primes(N):
    for num in range(1, N+1):
        for i in range(2, N):
            if (num % i) == 0:
                break
            else:
                print(num)

def get_primes(N):
    