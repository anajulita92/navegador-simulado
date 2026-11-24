from pathlib import Path
import re

from estrutura_web import EstruturaWeb


class CadastroURLs:
    """Valida, cadastra e persiste domínios e páginas da web simulada."""

    def __init__(self, diretorio_paginas="paginas", arquivo_urls="urls.txt"):
        self.__estrutura = EstruturaWeb()
        self.__urls = set()
        self.__diretorio_paginas = Path(diretorio_paginas)
        self.__arquivo_urls = Path(arquivo_urls)

    def normalizar_url(self, url):
        dominio, caminhos = EstruturaWeb.separar_url(url)
        return dominio + ("/" + "/".join(caminhos) if caminhos else "")

    def validar_url(self, url):
        dominio, caminhos = EstruturaWeb.separar_url(url)
        partes = dominio.split(".")
        if len(partes) < 2:
            raise ValueError("O domínio deve possuir partes separadas por ponto.")

        for parte in partes:
            if not parte or parte.startswith("-") or parte.endswith("-"):
                raise ValueError("Parte inválida no domínio.")
            if not all(c.isascii() and (c.isalnum() or c == "-") for c in parte):
                raise ValueError("O domínio contém caracteres inválidos.")
        return True

    def _caminho_arquivo(self, url):
        dominio, caminhos = EstruturaWeb.separar_url(url)
        base = self.__diretorio_paginas / dominio
        for parte in caminhos:
            base = base / parte
        return base / "index.txt"

    def esta_cadastrada(self, url):
        try:
            return self.__estrutura.buscar(url) is not None
        except ValueError:
            return False

    def adicionar(self, url, conteudo="Página cadastrada no navegador simulado."):
        self.validar_url(url)
        normalizada = self.normalizar_url(url)

        if normalizada in self.__urls:
            raise ValueError("A URL já está cadastrada.")

        arquivo = self._caminho_arquivo(normalizada)
        arquivo.parent.mkdir(parents=True, exist_ok=True)
        if arquivo.exists():
            raise ValueError("Já existe um arquivo para essa página.")

        arquivo.write_text(conteudo.rstrip() + "\n", encoding="utf-8")
        self.__estrutura.cadastrar(normalizada, str(arquivo))
        self.__urls.add(normalizada)
        self._salvar_urls()
        return normalizada

    def carregar_arquivo(self, caminho=None):
        origem = Path(caminho) if caminho else self.__arquivo_urls
        if not origem.exists():
            raise FileNotFoundError(f"Arquivo de URLs não encontrado: {origem}")

        for numero, linha in enumerate(origem.read_text(encoding="utf-8").splitlines(), start=1):
            url = linha.strip()
            if not url or url.startswith("#"):
                continue
            try:
                self.validar_url(url)
                normalizada = self.normalizar_url(url)
                if normalizada in self.__urls:
                    continue

                arquivo = self._caminho_arquivo(normalizada)
                arquivo.parent.mkdir(parents=True, exist_ok=True)
                if not arquivo.exists():
                    arquivo.write_text(
                        f"Bem-vindo à página simulada {normalizada}.\n",
                        encoding="utf-8"
                    )
                self.__estrutura.cadastrar(normalizada, str(arquivo))
                self.__urls.add(normalizada)
            except ValueError as erro:
                print(f"Linha {numero} ignorada em {origem}: {erro}")

    def _salvar_urls(self):
        self.__arquivo_urls.write_text(
            "".join(url + "\n" for url in sorted(self.__urls)),
            encoding="utf-8"
        )

    def obter_arquivo(self, url):
        return self.__estrutura.obter_arquivo(url)

    def obter_links(self, url):
        return self.__estrutura.obter_links(url)

    def listar_urls(self):
        return sorted(self.__urls)
