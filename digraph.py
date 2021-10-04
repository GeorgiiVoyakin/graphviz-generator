from graph import Graph


class Digraph(Graph):

    def __init__(self, data: list) -> None:
        super().__init__(data)

    def get_graphviz_data(self) -> str:
        '''
        Get genereted source code for graphviz
        '''
        result = 'digraph {\n'

        for i in range(len(self.data)):
            for j in range(len(self.data[i])):
                if self.data[i][j] > 0:
                    if self.has_path(i, j) and self.has_path(j, i):
                        if j < i:
                            result += '{} -> {} [label = "{weight}" weight = "{weight}" dir=both]\n'.format(i, j, weight=self.data[i][j])
                    else:
                        result += '{} -> {} [label = "{weight}" weight = "{weight}"]\n'.format(i, j, weight=self.data[i][j])

        result += '}\n'
        return result
