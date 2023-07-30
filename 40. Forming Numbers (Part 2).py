def forming_numbers_dp(digits, n):
  """
  Returns the number of ways to form n using the digits in digits.

  Args:
    digits: The digits to use.
    n: The number to form.

  Returns:
    The number of ways to form n using the digits in digits.
  """

  dp = [0 for i in range(n + 1)]
  dp[0] = 1
  for i in range(1, n + 1):
    for digit in digits:
      if i - digit >= 0:
        dp[i] += dp[i - digit]
  return dp[n]


def main():
  digits = [1, 2, 3]
  n = 5
  print(forming_numbers_dp(digits, n))


if __name__ == '__main__':
  main()
