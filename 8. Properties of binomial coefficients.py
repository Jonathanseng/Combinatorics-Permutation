def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def properties_of_binomial_coefficients():
    print("nC0 = 1")
    print("nC1 = n")
    print("nCn = 1")
    print("nCk = nCn-k")
    print("nCk = (n!) / (k!(n-k)!)")


if __name__ == "__main__":
    properties_of_binomial_coefficients()
