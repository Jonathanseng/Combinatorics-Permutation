def forming_numbers_memo(digits, n):
  """
  Returns the number of ways to form n using the digits in digits.

  Args:
    digits: The digits to use.
    n: The number to form.

  Returns:
    The number of ways to form n using the digits in digits.
  """

  memo = {}
  def dp(n):
    if n in memo:
      return memo[n]
    if n == 0:
      return 1
    else:
      count = 0
      for digit in digits:
        if n - digit >= 0:
          count += dp(n - digit)
      memo[n] = count
      return count
  return dp(n)


def main():
  digits = [1, 2, 3]
  n = 5
  print(forming_numbers_memo(digits, n))


if __name__ == '__main__':
  main()
