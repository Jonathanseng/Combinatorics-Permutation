def fibonacci(n):
  """
  Returns the nth Fibonacci number.

  Args:
    n: The index of the Fibonacci number to return.

  Returns:
    The nth Fibonacci number.
  """

  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return fibonacci(n - 1) + fibonacci(n - 2)


def main():
  print(fibonacci(0))
  print(fibonacci(1))
  print(fibonacci(2))
  print(fibonacci(3))
  print(fibonacci(4))


if __name__ == '__main__':
  main()
