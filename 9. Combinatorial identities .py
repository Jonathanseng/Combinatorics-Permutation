def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


def combinations(n, k):
    return factorial(n) / (factorial(k) * factorial(n - k))


def combinatorial_identities():
    print("nC0 + nC1 + ... + nCn = 2^n")
    print("nC0 * nCn + nC1 * nC(n-1) + ... + nC(n-1) * nC0 = n!")
    print("nCk = nC(n-k)")
    print("nCk * nC(n-k) = nCn")


if __name__ == "__main__":
    combinatorial_identities()
