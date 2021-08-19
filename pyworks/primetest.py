def count_primes(num):
    # Check for 0 or 1 input
    if num < 2:
        return 0
    ###############
    # 2 or greater
    ###############

    # Store our prime numbers
    primes = [2]

    # Counter going up to the input number.
    x = 3

    # x is going through every number upto input number.
    while x <= num:

        # Check if x is prime
        for y in range(3, x, 2):
            if x % y == 0:
                x += 2
                break
        # Unique to python having else on for loop.
        else:
            primes.append(x)
            x += 2

    print(primes)
    return len(primes)

count_primes(1000)