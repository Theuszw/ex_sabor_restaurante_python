class Avaliacao:
    def __init__(self, cliente, nota):
        self._cliente = cliente
        self._nota = nota


    def __dict__(self):
        return {
            'cliente': self._cliente,
            'nota': self._nota
        }