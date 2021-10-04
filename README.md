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

![Example of genereted graph](https://dreampuf.github.io/GraphvizOnline/#digraph%20%7B%0A0%20-%3E%201%20%5Blabel%20%3D%20%223%22%20weight%20%3D%20%223%22%5D%0A2%20-%3E%200%20%5Blabel%20%3D%20%225%22%20weight%20%3D%20%225%22%5D%0A2%20-%3E%201%20%5Blabel%20%3D%20%227%22%20weight%20%3D%20%227%22%20dir%3Dboth%5D%0A3%20-%3E%201%20%5Blabel%20%3D%20%228%22%20weight%20%3D%20%228%22%20dir%3Dboth%5D%0A%7D)
