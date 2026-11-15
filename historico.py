class No:
    def __init__(self, url, proximo=None):
        self.url = url
        self.proximo = proximo


class Historico:
    def __init__(self):
        self.__topo = None

    def empilhar(self, url):
        novo_no = No(url, self.__topo)
        self.__topo = novo_no

    def desempilhar(self):
        if self.__topo is None:
            return None
        url = self.__topo.url
        self.__topo = self.__topo.proximo
        return url

    def listar_cronologico(self):
        # Percorre a pilha e inverte para exibir do mais antigo ao mais recente
        urls = []
        atual = self.__topo
        while atual is not None:
            urls.append(atual.url)
            atual = atual.proximo
        return urls[::-1]