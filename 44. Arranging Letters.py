def arranging_letters(letters):
  """
  Returns the number of ways to arrange the letters in the string letters.

  Args:
    letters: The string of letters.

  Returns:
    The number of ways to arrange the letters in the string letters.
  """

  if len(letters) == 0:
    return 1
  else:
    count = 0
    for i in range(len(letters)):
      count += arranging_letters(letters[:i] + letters[i + 1:])
    return count


def main():
  letters = "abc"
  print(arranging_letters(letters))


if __name__ == '__main__':
  main()
