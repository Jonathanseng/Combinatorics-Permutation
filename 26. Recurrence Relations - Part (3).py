def fibonacci_dynamic_programming(n):
  """
  Returns the nth Fibonacci number, using dynamic programming.

  Args:
    n: The index of the Fibonacci number to return.

  Returns:
    The nth Fibonacci number.
  """

  fib_table = [0] * (n + 1)
  fib_table[0] = 0
  fib_table[1] = 1
  for i in range(2, n + 1):
    fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
  return fib_table[n]


def main():
  print(fibonacci_dynamic_programming(0))
  print(fibonacci_dynamic_programming(1))
  print(fibonacci_dynamic_programming(2))
  print(fibonacci_dynamic_programming(3))
  print(fibonacci_dynamic_programming(4))


if __name__ == '__main__':
  main()
