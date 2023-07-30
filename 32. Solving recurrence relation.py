def solve_recurrence_relation(a, b, c, x):
  """
  Solves the recurrence relation an = a * an-1 + b * an-2 + c.

  Args:
    a: The coefficient of an-1 in the recurrence relation.
    b: The coefficient of an-2 in the recurrence relation.
    c: The constant term in the recurrence relation.
    x: The variable that the generating function is in.

  Returns:
    The generating function for the solution to the recurrence relation.
  """

  g = 0
  f = c / (1 - a - b)
  for i in range(1, 100):
    g = g * x + f
    f = a * f + b * g
  return f / (1 - a - b)


def main():
  print(solve_recurrence_relation(1, 1, 1, x))


if __name__ == '__main__':
  main()
