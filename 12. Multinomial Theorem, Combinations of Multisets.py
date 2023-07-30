def multinomial_coefficient(n, k):
  """
  Returns the multinomial coefficient (n multichoose k).

  Args:
    n: The total number of objects.
    k: The number of objects in the first group.

  Returns:
    The multinomial coefficient (n multichoose k).
  """

  if k > n:
    raise ValueError("k cannot be greater than n")
  if k == 0:
    return 1
  else:
    return (n * multinomial_coefficient(n - 1, k - 1) +
            multinomial_coefficient(n - 1, k))


def combinations_of_multiset(n, k):
  """
  Returns a list of all combinations of k out of n, where repeated elements are allowed.

  Args:
    n: The total number of objects.
    k: The number of objects in the combination.

  Returns:
    A list of all combinations of k out of n, where repeated elements are allowed.
  """

  if k > n:
    raise ValueError("k cannot be greater than n")
  if k == 0:
    return [[]]
  else:
    combinations = []
    for i in range(n + 1):
      combinations.extend([*combination + [i], *combination])
    return combinations


def main():
  n = 3
  k = 2
  combinations = combinations_of_multiset(n, k)
  for combination in combinations:
    print(combination)


if __name__ == '__main__':
  main()
