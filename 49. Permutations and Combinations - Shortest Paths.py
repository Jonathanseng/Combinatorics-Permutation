def shortest_path(graph, start, end):
  """
  Returns the shortest path from start to end in graph.

  Args:
    graph: The graph.
    start: The start vertex.
    end: The end vertex.

  Returns:
    The shortest path from start to end in graph.
  """

  if start == end:
    return [start]
  else:
    shortest_paths = []
    for neighbor in graph[start]:
      path = shortest_path(graph, neighbor, end)
      if path is not None:
        path.append(start)
        shortest_paths.append(path)
    return min(shortest_paths, key=len)


def main():
  graph = {
    "A": ["B", "C"],
    "B": ["C", "D"],
    "C": ["D"],
    "D": []
  }
  start = "A"
  end = "D"
  print(shortest_path(graph, start, end))


if __name__ == '__main__':
  main()
