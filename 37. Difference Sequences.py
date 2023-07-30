def difference_sequence(sequence):
  """
  Returns the difference sequence of the given sequence.

  Args:
    sequence: The sequence to compute the difference sequence for.

  Returns:
    The difference sequence of the given sequence.
  """

  difference_sequence = []
  for i in range(1, len(sequence)):
    difference_sequence.append(sequence[i] - sequence[i - 1])
  return difference_sequence


def main():
  sequence = [1, 2, 3, 5, 8, 13]
  print(difference_sequence(sequence))


if __name__ == '__main__':
  main()
