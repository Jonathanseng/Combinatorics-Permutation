import itertools


def inclusion_exclusion_part4(sets):
  """
  Returns the cardinality of the union of the given sets.

  Args:
    sets: A list of sets.

  Returns:
    The cardinality of the union of the given sets.
  """

  result = sum(len(set) for set in sets)
  for k in range(2, len(sets) + 1):
    combs = itertools.combinations(sets, k)
    result -= sum(len(set.intersection(*comb)) for comb in combs)
  return result


def main():
  sets = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
  print(inclusion_exclusion_part4(sets))


if __name__ == '__main__':
  main()
