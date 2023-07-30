def fibonacci_bottom_up(n):
  """
  Returns the nth Fibonacci number, using bottom-up dynamic programming.

  Args:
    n: The index of the Fibonacci number to return.

  Returns:
    The nth Fibonacci number.
  """

  fib_table = [0] * (n + 1)
  for i in range(n + 1):
    if i == 0 or i == 1:
      fib_table[i] = i
    else:
      fib_table[i] = fib_table[i - 1] + fib_table[i - 2]
  return fib_table[n]


def main():
  print(fibonacci_bottom_up(0))
  print(fibonacci_bottom_up(1))
  print(fibonacci_bottom_up(2))
  print(fibonacci_bottom_up(3))
  print(fibonacci_bottom_up(4))


if __name__ == '__main__':
  main()
