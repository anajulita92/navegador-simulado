class NoPagina:
    """Nó da árvore que representa um domínio ou uma página interna."""

    def __init__(self):
        self.filhos = {}
        self.arquivo = None


class EstruturaWeb:
    """Árvore de domínios e páginas, com no máximo dois links por página."""

    LIMITE_LINKS = 2

    def __init__(self):
        self.__dominios = {}

    @staticmethod
    def separar_url(url):
        if not isinstance(url, str) or not url.strip():
            raise ValueError("A URL não pode estar vazia.")

        endereco = url.strip()
        esquema = endereco.lower()
        if esquema.startswith("https://"):
            endereco = endereco[8:]
        elif esquema.startswith("http://"):
            endereco = endereco[7:]

        if "://" in endereco or any(c in endereco for c in "?#\\"):
            raise ValueError("Protocolo, parâmetros, fragmentos ou barras inválidos.")

        if endereco.endswith("/"):
            endereco = endereco[:-1]
        if not endereco or endereco.endswith("/"):
            raise ValueError("A URL contém um caminho vazio.")

        partes = endereco.split("/")
        dominio = partes[0].lower()
        caminhos = partes[1:]

        if not dominio or any(not parte for parte in caminhos):
            raise ValueError("Domínio ou caminho interno inválido.")

        for parte in caminhos:
            if parte in (".", ".."):
                raise ValueError("Caminho interno inválido.")
            if not all(c.isalnum() or c in "-_." for c in parte):
                raise ValueError("O caminho contém caracteres não permitidos.")

        return dominio, caminhos

    def validar_cadastro(self, url):
        """Verifica o limite de ramificações sem alterar a árvore."""
        dominio, caminhos = self.separar_url(url)
        atual = self.__dominios.get(dominio)

        if atual is None:
            return True

        for caminho in caminhos:
            proximo = atual.filhos.get(caminho)
            if proximo is None:
                if len(atual.filhos) >= self.LIMITE_LINKS:
                    raise ValueError(
                        f"Cada página pode ter no máximo {self.LIMITE_LINKS} links internos."
                    )
                return True
            atual = proximo

        return True

    def cadastrar(self, url, arquivo=None):
        dominio, caminhos = self.separar_url(url)
        self.validar_cadastro(url)

        if dominio not in self.__dominios:
            self.__dominios[dominio] = NoPagina()

        atual = self.__dominios[dominio]
        for caminho in caminhos:
            if caminho not in atual.filhos:
                atual.filhos[caminho] = NoPagina()
            atual = atual.filhos[caminho]

        if arquivo is not None:
            atual.arquivo = arquivo
        return atual

    def buscar(self, url):
        dominio, caminhos = self.separar_url(url)
        atual = self.__dominios.get(dominio)
        if atual is None:
            return None

        for caminho in caminhos:
            atual = atual.filhos.get(caminho)
            if atual is None:
                return None
        return atual

    def obter_links(self, url):
        pagina = self.buscar(url)
        if pagina is None:
            return []
        return [
            "/" + nome
            for nome, filho in sorted(pagina.filhos.items())
            if filho.arquivo is not None
        ]

    def obter_arquivo(self, url):
        pagina = self.buscar(url)
        return None if pagina is None else pagina.arquivo

    def listar_dominios(self):
        return sorted(self.__dominios)
