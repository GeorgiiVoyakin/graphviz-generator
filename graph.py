class Graph:

    def __init__(self, data: list) -> None:
        self.data = data

    def __str__(self) -> str:
        return 'Data: {}'.format(self.data.__str__())

    def has_path(self, source: int, dest: int) -> bool:
        '''
        Returns True if there is path form source vertex to dest vertex 
        '''
        return self.data[source][dest] > 0 

    def has_connection(self, vertex_a: int, vertex_b: int) -&gt; bool:
        '''
        Returns True if vertex_a has edge to vertex_b
        '''
        return self.data[vertex_a][vertex_b] > 0 or self.data[vertex_b][vertex_a] > 0
