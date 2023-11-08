def find_prime_factors(number):

    divisor  = 2
    while divisor <= number:
        if number % divisor == 0:
           return divisor
        else:
            divisor += 1
number = int(input("Enter a number: "))

prime_factor = find_prime_factors(number)
print(f"The prime factor of {number} is {prime_factor}")
