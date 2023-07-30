import math


def sterling_formula(n):
  """
  Returns the value of Sterling's formula for n.

  Args:
    n: The number.

  Returns:
    The value of Sterling's formula for n.
  """

  if n == 0:
    return 0
  else:
    return math.sqrt(2 * math.pi * n) * (n / math.e)**n * (1 + 1 / (12 * n))


def main():
  n = 5
  value = sterling_formula(n)
  print("The value of Sterling's formula for n = {} is {}".format(n, value))


if __name__ == '__main__':
  main()
