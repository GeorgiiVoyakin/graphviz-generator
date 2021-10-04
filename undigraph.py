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
                if j > 0:
                    result += '{} -- {}\n'.format(i, j)
                else:
                    result += '{}\n'.format(j)

        result += '}\n'
        return result
