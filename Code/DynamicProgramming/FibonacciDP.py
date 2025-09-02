# Number of times we calculated through the function,
# uncomment/comment which one you want/don't want to see
calculations = 0


# Naive recursive Fibonacci - O(2^n)
def fibonacci(n):
    # global calculations
    # calculations += 1
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# Memoized Fibonacci - O(n)
def fibonacci_master():
    cache = {}

    def fib(n):
        global calculations
        calculations += 1
        if n in cache:
            return cache[n]
        else:
            if n <= 1:
                return n
            else:
                cache[n] = fib(n - 1) + fib(n - 2)
                return cache[n]

    return fib


# Bottom-up Fibonacci - O(n)
def fibonacci_master2(n):
    if n < 2:
        return n
    answer = [0, 1]
    for i in range(2, n + 1):
        # global calculations
        # calculations += 1
        answer.append(answer[i - 2] + answer[i - 1])
    return answer[-1]


def main():
    faster_fib = fibonacci_master()
    print("Slow:", fibonacci(10))
    print("DP:", faster_fib(10))
    print("DP2:", fibonacci_master2(10))
    print(f"We did {calculations} calculations")


if __name__ == '__main__':
    main()
