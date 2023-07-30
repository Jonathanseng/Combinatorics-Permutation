def permutations_circular(n):
  """
  Returns the number of permutations of n elements in a circle.

  Args:
    n: The number of elements.

  Returns:
    The number of permutations of n elements in a circle.
  """

  if n == 0:
    return 1
  else:
    return factorial(n - 1)


def combinations_circular(n, k):
  """
  Returns the number of combinations of n elements taken k at a time in a circle.

  Args:
    n: The number of elements.
    k: The number of elements to take.

  Returns:
    The number of combinations of n elements taken k at a time in a circle.
  """

  if k > n:
    raise ValueError("k must be less than or equal to n")
  else:
    return factorial(n - 1) / factorial(k) / factorial(n - k - 1)


def main():
  n = 5
  k = 3
  print(permutations_circular(n))
  print(combinations_circular(n, k))


if __name__ == '__main__':
  main()
