def bijective_proof(n):
    injective_map = {}
    surjective_map = {}
    for i in range(n + 1):
        injective_map[i] = i ** 2
        surjective_map[i ** 2] = i
    return injective_map, surjective_map


def main():
    injective_map, surjective_map = bijective_proof(5)
    print(injective_map)
    print(surjective_map)


if __name__ == "__main__":
    main()
