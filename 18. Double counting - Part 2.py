def double_counting_part2(n, k):
  """
  Returns the value of the double counting function for n and k.

  Args:
    n: The total number of objects.
    k: The number of objects in the first group.

  Returns:
    The value of the double counting function for n and k.
  """

  if k > n:
    raise ValueError("k cannot be greater than n")
  if k == 0:
    return 1
  else:
    return (n * k + k * (k - 1)) / 2


def main():
  n = 5
  k = 2
  value = double_counting_part2(n, k)
  print("The value of the double counting function for n = {} and k = {} is {}".format(n, k, value))


if __name__ == '__main__':
  main()
