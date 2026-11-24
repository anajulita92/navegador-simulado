class No:
    def __init__(self, url, proximo=None):
        self.url = url
        self.proximo = proximo


class Historico:
    """Pilha encadeada: o último endereço empilhado é o primeiro removido."""

    def __init__(self):
        self.__topo = None

    def empilhar(self, url):
        self.__topo = No(url, self.__topo)

    def desempilhar(self):
        if self.__topo is None:
            return None
        url = self.__topo.url
        self.__topo = self.__topo.proximo
        return url

    def listar_cronologico(self):
        urls = []
        atual = self.__topo
        while atual is not None:
            urls.append(atual.url)
            atual = atual.proximo
        return urls[::-1]
