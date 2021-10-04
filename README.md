# graphviz-generator
Python classes to generate graphviz source code for undirected and directed graph

## Example
```python3
from digraph import Digraph

matrix = [
    [0, 3, -1, -1],
    [-1, 0, 7, 8],
    [5, 7, 0, -1],
    [-1, 8, -1, 0]
]

g = Digraph(matrix)

print(g.get_graphviz_data())
```
### Output
```text
digraph {
0 -> 1 [label = "3" weight = "3"]
2 -> 0 [label = "5" weight = "5"]
2 -> 1 [label = "7" weight = "7" dir=both]
3 -> 1 [label = "8" weight = "8" dir=both]
}
```

![Example of genereted graph](https://raw.githubusercontent.com/GeorgiiVoyakin/graphviz-generator/f0e59d476b8c8acb68ddc93ddb1f9a1cb9c55f07/graphviz.png)
