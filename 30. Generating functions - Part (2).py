def fibonacci_generating_function_closed_form(x):
  """
  Returns the closed-form expression for the generating function of the Fibonacci sequence.

  Args:
    x: The variable that the generating function is in.

  Returns:
    The closed-form expression for the generating function of the Fibonacci sequence.
  """

  return (1 - x) / (1 - x ** 2)


def main():
  print(fibonacci_generating_function_closed_form(x))


if __name__ == '__main__':
  main()
