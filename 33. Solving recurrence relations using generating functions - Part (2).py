def fibonacci_generating_function_closed_form(x):
  """
  Returns the closed-form expression for the generating function of the Fibonacci sequence.

  Args:
    x: The variable that the generating function is in.

  Returns:
    The closed-form expression for the generating function of the Fibonacci sequence.
  """

  return (1 - x) / (1 - x ** 2)


def solve_recurrence_relation_closed_form(a, b, c, x):
  """
  Solves the recurrence relation an = a * an-1 + b * an-2 + c.

  Args:
    a: The coefficient of an-1 in the recurrence relation.
    b: The coefficient of an-2 in the recurrence relation.
    c: The constant term in the recurrence relation.
    x: The variable that the generating function is in.

  Returns:
    The closed-form expression for the solution to the recurrence relation.
  """

  return (c - b * x) / (1 - a - b)


def main():
  print(solve_recurrence_relation_closed_form(1, 1, 1, x))


if __name__ == '__main__':
  main()
