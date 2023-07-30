def selection(array, low, high):
  """
  Recursively selects the kth smallest element in the array.

  Args:
    array: The array to search.
    low: The index of the first element in the array.
    high: The index of the last element in the array.

  Returns:
    The kth smallest element in the array.
  """

  if high <= low:
    return array[low]
  else:
    pivot = array[high]
    i = low - 1
    for j in range(low, high):
      if array[j] <= pivot:
        i += 1
        array[i], array[j] = array[j], array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return selection(array, low, i)


def main():
  array = [10, 5, 2, 7, 3, 1, 8, 9, 6, 4]
  k = 5
  print(selection(array, 0, len(array) - 1))


if __name__ == '__main__':
  main()
