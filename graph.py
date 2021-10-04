class Graph:

    def __init__(self, data: list) -> None:
        self.data = data

    def __str__(self) -> str:
        return 'Data: {}'.format(self.data.__str__())
