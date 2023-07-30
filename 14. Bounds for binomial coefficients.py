def bounds_for_binomial_coefficients(n, k):
  """
  Returns the lower and upper bounds for the binomial coefficient (n choose k).

  Args:
    n: The total number of objects.
    k: The number of objects in the first group.

  Returns:
    A tuple of the lower and upper bounds for the binomial coefficient (n choose k).
  """

  if k > n:
    raise ValueError("k cannot be greater than n")
  if k == 0:
    return (0, 1)
  else:
    lower_bound = (1.0 * k) / n
    upper_bound = (1.0 * k) / (n - k + 1)
    return (lower_bound, upper_bound)


def main():
  n = 5
  k = 2
  lower_bound, upper_bound = bounds_for_binomial_coefficients(n, k)
  print("Lower bound:", lower_bound)
  print("Upper bound:", upper_bound)


if __name__ == '__main__':
  main()
