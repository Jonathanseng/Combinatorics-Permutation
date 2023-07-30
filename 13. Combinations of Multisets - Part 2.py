def combinations_of_multiset_part2(elements, k):
  """
  Returns a list of all combinations of k out of n, where repeated elements are allowed.

  Args:
    elements: A list of elements in the multiset.
    k: The number of elements in the combination.

  Returns:
    A list of all combinations of k out of n, where repeated elements are allowed.
  """

  if k > len(elements):
    raise ValueError("k cannot be greater than the length of the multiset")
  if k == 0:
    return [[]]
  else:
    combinations = []
    for i in range(len(elements)):
      combinations.extend(
          [[elements[i]] + combination
           for combination in combinations_of_multiset_part2(elements[i + 1:], k - 1)])
    return combinations


def main():
  elements = ['a', 'b', 'c', 'b']
  k = 2
  combinations = combinations_of_multiset_part2(elements, k)
  for combination in combinations:
    print(combination)


if __name__ == '__main__':
  main()
