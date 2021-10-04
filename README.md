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
digraph {
0 -> 1 [label = "3" weight = "3"]
2 -> 0 [label = "5" weight = "5"]
2 -> 1 [label = "7" weight = "7" dir=both]
3 -> 1 [label = "8" weight = "8" dir=both]
}

![Example of genereted graph](https://bit.ly/3Dau5Uv)
