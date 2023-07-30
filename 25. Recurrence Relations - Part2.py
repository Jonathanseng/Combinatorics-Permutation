def fibonacci_memoization(n):
  """
  Returns the nth Fibonacci number, using memoization to avoid recomputation.

  Args:
    n: The index of the Fibonacci number to return.

  Returns:
    The nth Fibonacci number.
  """

  fib_memo = {}
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    if n not in fib_memo:
      fib_memo[n] = fibonacci_memoization(n - 1) + fibonacci_memoization(n - 2)
    return fib_memo[n]


def main():
  print(fibonacci_memoization(0))
  print(fibonacci_memoization(1))
  print(fibonacci_memoization(2))
  print(fibonacci_memoization(3))
  print(fibonacci_memoization(4))


if __name__ == '__main__':
  main()
