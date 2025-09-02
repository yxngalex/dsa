#   To build a recursive function you need 3 rules:
#   1. Identify the base case
#   2. Identify the recursive case
#   3. Get closer and closer and return when needed. Usually you have 2 returns.

# 5! = 5 * 4 * 3 * 2 * 1
# 5! = 5 * 4!
# 5! = 5 * 4 * 3!
def factorial_recursive(n):  # O(n)
    if n < 2:
        return 1
    return n * factorial_recursive(n - 1)


def factorial_iterative(n):  # O(n)
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def factorial(n):
    print('recursive: ', factorial_recursive(n))
    print('iterative: ', factorial_iterative(n))


def main():
    factorial(4)


if __name__ == '__main__':
    main()
