from cadastro_urls import CadastroURLs
from historico import Historico


class Navegador:
    def __init__(self, cadastro):
        self.__cadastro = cadastro
        self.__historico = Historico()
        self.__pagina_atual = None

    @property
    def pagina_atual(self):
        return self.__pagina_atual

    def acessar(self, url):
        # Confere o destino antes de mudar a navegação
        self.__cadastro.validar_url(url)

        if not self.__cadastro.esta_cadastrada(url):
            raise ValueError("Página não encontrada.")

        # No primeiro acesso, ainda não existe página para guardar
        if self.__pagina_atual is not None:
            self.__historico.empilhar(self.__pagina_atual)

        self.__pagina_atual = url

    def voltar(self):
        pagina_anterior = self.__historico.desempilhar()

        # Se não houver página anterior, mantém a atual
        if pagina_anterior is None:
            return None

        self.__pagina_atual = pagina_anterior
        return pagina_anterior

    def listar_historico(self):
        return self.__historico.listar()


if __name__ == "__main__":
    cadastro = CadastroURLs()
    cadastro.adicionar("www.ifpb.edu.br")
    cadastro.adicionar("www.python.org")

    navegador = Navegador(cadastro)

    navegador.acessar("www.ifpb.edu.br")
    navegador.acessar("www.python.org")

    print("Atual:", navegador.pagina_atual)
    print("Histórico:", navegador.listar_historico())

    try:
        navegador.acessar("www.exemplo.com")
    except ValueError as erro:
        print("Erro:", erro)

    print("Atual após tentativa inválida:", navegador.pagina_atual)
    print("Histórico após tentativa inválida:", navegador.listar_historico())

    print("Voltar:", navegador.voltar())
    print("Atual:", navegador.pagina_atual)
    print("Histórico:", navegador.listar_historico())
    print("Voltar sem histórico:", navegador.voltar())
    print("Atual:", navegador.pagina_atual)