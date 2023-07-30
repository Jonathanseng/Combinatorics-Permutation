def permutations(n, k):
  """
  Returns the number of permutations of n elements taken k at a time.

  Args:
    n: The number of elements.
    k: The number of elements to take.

  Returns:
    The number of permutations of n elements taken k at a time.
  """

  if k > n:
    raise ValueError("k must be less than or equal to n")
  else:
    return factorial(n) / factorial(n - k)


def combinations(n, k):
  """
  Returns the number of combinations of n elements taken k at a time.

  Args:
    n: The number of elements.
    k: The number of elements to take.

  Returns:
    The number of combinations of n elements taken k at a time.
  """

  if k > n:
    raise ValueError("k must be less than or equal to n")
  else:
    return factorial(n) / factorial(k) / factorial(n - k)


def main():
  n = 5
  k = 3
  print(permutations(n, k))
  print(combinations(n, k))


if __name__ == '__main__':
  main()
