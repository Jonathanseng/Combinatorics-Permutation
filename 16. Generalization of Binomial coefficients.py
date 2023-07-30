def generalized_binomial_coefficient(n, k, p):
  """
  Returns the value of the generalized binomial coefficient (n choose k, p).

  Args:
    n: The total number of objects.
    k: The number of objects in the first group.
    p: The probability of success.

  Returns:
    The value of the generalized binomial coefficient (n choose k, p).
  """

  if k > n:
    raise ValueError("k cannot be greater than n")
  if k == 0:
    return 1
  else:
    return (p**k) * ((1 - p)**(n - k))


def main():
  n = 5
  k = 2
  p = 0.5
  value = generalized_binomial_coefficient(n, k, p)
  print("The value of the generalized binomial coefficient (n choose k, p) for n = {} k = {} p = {} is {}".format(n, k, p, value))


if __name__ == '__main__':
  main()
