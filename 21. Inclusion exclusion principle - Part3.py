def inclusion_exclusion_part3(sets):
  """
  Returns the cardinality of the union of the given sets.

  Args:
    sets: A list of sets.

  Returns:
    The cardinality of the union of the given sets.
  """

  result = 0
  for set in sets:
    result += len(set)
  for i in range(len(sets)):
    for j in range(i + 1, len(sets)):
      if sets[i] & sets[j]:
        result -= 2 * len(sets[i] & sets[j])
  return result


def main():
  sets = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
  print(inclusion_exclusion_part3(sets))


if __name__ == '__main__':
  main()
