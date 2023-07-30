def arranging_people(n):
  """
  Returns the number of ways to arrange n people in a line.

  Args:
    n: The number of people.

  Returns:
    The number of ways to arrange n people in a line.
  """

  if n == 0:
    return 1
  else:
    return n * arranging_people(n - 1)


def main():
  n = 5
  print(arranging_people(n))


if __name__ == '__main__':
  main()
