class No:
    def __init__(self, url, proximo=None):
        self.url = url
        self.proximo = proximo


class Historico:
    def __init__(self):
        self.__topo = None

    def empilhar(self, url):
        # O novo nó aponta para o topo anterior
        novo_no = No(url, self.__topo)
        self.__topo = novo_no

    def desempilhar(self):
        if self.__topo is None:
            return None

        # Guarda o endereço e passa o topo para o próximo nó
        url = self.__topo.url
        self.__topo = self.__topo.proximo
        return url

    def listar(self):
        urls = []
        atual = self.__topo

        # Percorre os nós sem alterar o histórico
        while atual is not None:
            urls.append(atual.url)
            atual = atual.proximo

        return urls


if __name__ == "__main__":
    historico = Historico()

    historico.empilhar("www.ifpb.edu.br")
    historico.empilhar("www.python.org")

    print(historico.listar())
    print(historico.desempilhar())
    print(historico.listar())
    print(historico.desempilhar())
    print(historico.desempilhar())