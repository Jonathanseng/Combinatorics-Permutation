def s(n, k):
  """
  Returns the Stirling number of the second kind of n and k.

  Args:
    n: The number of objects.
    k: The number of groups.

  Returns:
    The Stirling number of the second kind of n and k.
  """

  if k > n:
    raise ValueError("k must be less than or equal to n")
  if k == 0:
    return 1
  else:
    return (n - k + 1) * s(n - 1, k - 1) + k * s(n - 1, k)


def main():
  print(s(5, 3))


if __name__ == '__main__':
  main()
