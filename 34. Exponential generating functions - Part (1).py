def fibonacci_exponential_generating_function(x):
  """
  Returns the exponential generating function for the Fibonacci sequence.

  Args:
    x: The variable that the generating function is in.

  Returns:
    The exponential generating function for the Fibonacci sequence.
  """

  f = 0
  g = 1
  for i in range(1, 100):
    f = f * x + g
    g = f + g * x
  return f * (1 - x) ** (-2)


def main():
  print(fibonacci_exponential_generating_function(x))


if __name__ == '__main__':
  main()
