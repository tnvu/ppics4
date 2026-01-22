# Write a function to compute the nth Fibonacci number. Use your function
# to solve Programming Exercise 16 from Chapter 3.

def fib(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a+b
    return a

def main():
    n = int(input("Find nth Fibonacci number: "))
    answer = fib(n)
    print("Nth Fibonacci number = ", answer)

main()
