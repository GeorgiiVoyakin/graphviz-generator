from graph import Graph


class UndiGraph(Graph):

    def __init__(self, data: list) -> None:
        super().__init__(data)

    def get_graphviz_data(self) -> str:
        '''
        Get genereted source code for graphviz
        '''
        result = 'graph {\n'

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] > 0 and j < i:
                    result += '{} -- {} [label = "{weight}" weight = "{weight}"]\n'.format(
                        i, j, weight=self.data[i][j])
                    self.edges[i] = j

        result += '}\n'
        return result
