def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def main():
    print(combinations(5, 2))
    print(combinations(10, 5))


if __name__ == "__main__":
    main()
