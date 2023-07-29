def pigeonhole_principle_2(n, k):
    if n <= k:
        return "All pigeons can have their own hole"
    else:
        return "At least two pigeons must share a hole"


def main():
    print(pigeonhole_principle_2(3, 2))
    print(pigeonhole_principle_2(3, 3))


if __name__ == "__main__":
    main()
