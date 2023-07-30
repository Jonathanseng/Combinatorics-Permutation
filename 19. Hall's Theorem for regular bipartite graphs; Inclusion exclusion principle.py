def hall_theorem(graph):
  """
  Returns True if Hall's Theorem holds for the given graph, and False otherwise.

  Args:
    graph: A bipartite graph.

  Returns:
    True if Hall's Theorem holds for the given graph, and False otherwise.
  """

  n = len(graph[0])
  m = len(graph[1])
  for i in range(n):
    count = 0
    for j in range(m):
      if graph[0][i] == graph[1][j]:
        count += 1
    if count < i + 1:
      return False
  return True


def inclusion_exclusion(sets):
  """
  Returns the cardinality of the union of the given sets.

  Args:
    sets: A list of sets.

  Returns:
    The cardinality of the union of the given sets.
  """

  result = 0
  for set in sets:
    result += len(set)
  for i in range(len(sets)):
    for j in range(i + 1, len(sets)):
      if sets[i] & sets[j]:
        result -= len(sets[i] & sets[j])
  return result


def main():
  graph = [[0, 1, 2], [0, 1, 2]]
  print(hall_theorem(graph))

  sets = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
  print(inclusion_exclusion(sets))


if __name__ == '__main__':
  main()
