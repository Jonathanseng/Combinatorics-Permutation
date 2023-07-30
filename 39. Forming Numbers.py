def forming_numbers(digits, n):
  """
  Returns the number of ways to form n using the digits in digits.

  Args:
    digits: The digits to use.
    n: The number to form.

  Returns:
    The number of ways to form n using the digits in digits.
  """

  if n < 0:
    return 0
  if n == 0:
    return 1
  else:
    count = 0
    for i in range(len(digits)):
      if n - digits[i] >= 0:
        count += forming_numbers(digits, n - digits[i])
    return count


def main():
  digits = [1, 2, 3]
  n = 5
  print(forming_numbers(digits, n))


if __name__ == '__main__':
  main()
