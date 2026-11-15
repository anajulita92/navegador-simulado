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
        self.__cadastro.validar_url(url)

        if not self.__cadastro.esta_cadastrada(url):
            raise ValueError("Erro 404: Página não encontrada!")

        if self.__pagina_atual is not None:
            self.__historico.empilhar(self.__pagina_atual)

        self.__pagina_atual = url

    def voltar(self):
        pagina_anterior = self.__historico.desempilhar()
        if pagina_anterior is None:
            return None
        self.__pagina_atual = pagina_anterior
        return pagina_anterior

    def obter_historico_formatado(self):
        lista = self.__historico.listar_cronologico()
        return "".join([f"[{u}]" for u in lista])