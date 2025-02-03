def countdown(n):
    print(n)

    if n <= 0:
        return

    countdown(n - 1)

print(countdown(5))


def factorial(n):
    if n == 1:
        return 1

    return n * factorial(n - 1)

print()

fact_input = 5
print(f"{fact_input} factorial: ", factorial(fact_input))