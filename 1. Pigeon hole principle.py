def pigeonhole_principle(n, k):
    if n > k:
        raise ValueError("n must be less than or equal to k")
    return "At least two pigeons must share a hole"


def main():
    print(pigeonhole_principle(3, 2))


if __name__ == "__main__":
    main()
