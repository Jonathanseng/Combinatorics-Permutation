def is_anagram(word1, word2):
  """
  Returns True if word1 and word2 are anagrams, False otherwise.

  Args:
    word1: The first word.
    word2: The second word.

  Returns:
    True if word1 and word2 are anagrams, False otherwise.
  """

  if len(word1) != len(word2):
    return False
  else:
    count = {}
    for letter in word1:
      if letter in count:
        count[letter] += 1
      else:
        count[letter] = 1
    for letter in word2:
      if letter not in count:
        return False
      else:
        count[letter] -= 1
    for value in count.values():
      if value != 0:
        return False
    return True


def main():
  word1 = "hello"
  word2 = "olleh"
  print(is_anagram(word1, word2))


if __name__ == '__main__':
  main()
