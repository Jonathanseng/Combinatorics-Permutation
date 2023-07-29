def permutations_of_multisets(elements):
    if len(elements) == 0:
        return [[]]
    else:
        permutations = []
        for i in range(len(elements)):
            sub_permutations = permutations_of_multisets(elements[:i] + elements[i + 1:])
            for permutation in sub_permutations:
                permutations.append([elements[i]] + permutation)
        return permutations


def main():
    elements = ["a", "a", "b"]
    permutations = permutations_of_multisets(elements)
    for permutation in permutations:
        print(permutation)


if __name__ == "__main__":
    main()
