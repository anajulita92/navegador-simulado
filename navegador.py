from pathlib import Path

from historico import Historico
from estrutura_web import EstruturaWeb


class Navegador:
    """Controla a página atual, a navegação e o histórico."""

    def __init__(self, cadastro):
        self.__cadastro = cadastro
        self.__historico = Historico()
        self.__pagina_atual = None

    @property
    def pagina_atual(self):
        return self.__pagina_atual

    def _resolver_endereco(self, url):
        if not isinstance(url, str) or not url.strip():
            raise ValueError("Digite um endereço.")

        entrada = url.strip()
        if entrada.startswith("/"):
            if self.__pagina_atual is None:
                raise ValueError("Acesse um domínio antes de navegar para uma página interna.")
            if entrada == "/":
                dominio, _ = EstruturaWeb.separar_url(self.__pagina_atual)
                return dominio
            if entrada.startswith("//") or entrada.endswith("/") or "//" in entrada:
                raise ValueError("Caminho interno inválido.")

            dominio, caminhos_atuais = EstruturaWeb.separar_url(self.__pagina_atual)
            prefixo = "/".join(caminhos_atuais)
            caminho_completo = "/".join(parte for parte in (prefixo, entrada[1:]) if parte)
            return dominio + "/" + caminho_completo

        return self.__cadastro.normalizar_url(entrada)

    def acessar(self, url):
        destino = self._resolver_endereco(url)
        self.__cadastro.validar_url(destino)

        if not self.__cadastro.esta_cadastrada(destino):
            raise ValueError("Erro 404: Página não encontrada!")

        if self.__pagina_atual is not None:
            self.__historico.empilhar(self.__pagina_atual)

        self.__pagina_atual = destino
        return destino

    def voltar(self):
        anterior = self.__historico.desempilhar()
        if anterior is None:
            return None
        self.__pagina_atual = anterior
        return anterior

    def obter_historico_formatado(self):
        return "".join(f"[{url}]" for url in self.__historico.listar_cronologico())

    def exibir_pagina_atual(self):
        if self.__pagina_atual is None:
            print("Nenhuma página aberta.")
            return

        arquivo = self.__cadastro.obter_arquivo(self.__pagina_atual)
        if arquivo is None or not Path(arquivo).is_file():
            print("Erro 404: arquivo da página não encontrado.")
            return

        conteudo = Path(arquivo).read_text(encoding="utf-8")
        print("\n" + "-" * 50)
        print(f"url: {self.__pagina_atual}")
        print(conteudo.rstrip())

        links = self.__cadastro.obter_links(self.__pagina_atual)
        if links:
            print("\nLinks disponíveis:")
            for link in links:
                print(link)
        print("-" * 50)
