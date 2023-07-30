def permutations_of_multiset_part2(elements):
  """
  Returns a list of all permutations of the given multiset, in lexicographical order.

  Args:
    elements: A list of elements in the multiset.

  Returns:
    A list of all permutations of the given multiset, in lexicographical order.
  """

  if not elements:
    return [[]]

  first_element = elements.pop(0)
  permutations_of_remaining_elements = permutations_of_multiset_part2(elements)
  permutations = []
  for permutation in permutations_of_remaining_elements:
    for i in range(len(permutation) + 1):
      new_permutation = permutation[:i] + [first_element] + permutation[i:]
      if new_permutation not in permutations:
        permutations.append(new_permutation)
  return permutations


def main():
  elements = ['a', 'b', 'c', 'b']
  permutations = permutations_of_multiset_part2(elements)
  for permutation in permutations:
    print(permutation)


if __name__ == '__main__':
  main()
