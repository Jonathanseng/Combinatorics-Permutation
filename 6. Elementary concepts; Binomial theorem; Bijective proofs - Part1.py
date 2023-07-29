def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def binomial_theorem(n, k):
    return combinations(n, k) * (n ** k) * (1 ** (n - k))


def main():
    print(binomial_theorem(5, 2))
    print(binomial_theorem(10, 5))


if __name__ == "__main__":
    main()
