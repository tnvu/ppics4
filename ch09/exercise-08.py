# The Sieve of Eratosthenes is an elegant algorithm for finding all of the
# prime numbers up to some limit n. The basic idea is to first create a list
# of numbers from 2 to n. The first number is removed from the list and
# announced as a prime number, and all multiples of this number up to n
# are removed from the list. This process continues until the list is empty.
# For example, if we wished to find all the primes up to 10, the list
# would originally contain 2, 3, 4, 5, 6, 7, 8, 9, 10. The 2 is removed
# and announced to be prime. Then 4, 6, 8, and 10 are removed, since
# they are multiples of 2. That leaves 3, 5, 7, 9. Repeating the process,
# 3 is announced as prime and removed, and 9 is removed because it is a
# multiple of 3. That leaves 5 and 7. The algorithm continues by announcing
# that 5 is prime and removing it from the list. Finally, 7 is announced and
# removed, and we’re done.
# Write a program that prompts a user for n and then uses the sieve
# algorithm to find all the primes less than or equal to n.

def sieveOfEratosthenes(n):
    l = list(range(2, n+1))
    primes = []
    while True:
        if len(l) == 0:
            break
        prime = l.pop(0)
        l = [n for n in l if n % prime != 0]
        primes.append(prime)
    return primes

def main():
    n = int(input("Enter n: "))
    primes = sieveOfEratosthenes(n)
    print(f"Primes = {primes}")

main()