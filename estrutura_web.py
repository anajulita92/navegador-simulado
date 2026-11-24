class NoPagina:
    """Nó da árvore que representa uma página da web simulada."""

    def __init__(self):
        self.filhos = {}
        self.arquivo = None


class EstruturaWeb:
    """Organiza domínios e páginas internas em uma árvore de dicionários."""

    def __init__(self):
        self.__dominios = {}

    @staticmethod
    def separar_url(url):
        if not isinstance(url, str) or not url.strip():
            raise ValueError("A URL não pode estar vazia.")

        endereco = url.strip()
        if endereco.startswith("https://"):
            endereco = endereco[8:]
        elif endereco.startswith("http://"):
            endereco = endereco[7:]

        if "://" in endereco or "?" in endereco or "#" in endereco:
            raise ValueError("Protocolo, parâmetros ou fragmentos inválidos.")

        endereco = endereco.rstrip("/")
        partes = endereco.split("/")
        dominio = partes[0].lower()
        caminhos = partes[1:]

        if not dominio or any(not parte for parte in caminhos):
            raise ValueError("Domínio ou caminho interno inválido.")

        for parte in caminhos:
            if parte in (".", "..") or "\\" in parte:
                raise ValueError("Caminho interno inválido.")
            if not all(c.isascii() and (c.isalnum() or c in "-_.") for c in parte):
                raise ValueError("O caminho contém caracteres não permitidos.")

        return dominio, caminhos

    def cadastrar(self, url, arquivo=None):
        dominio, caminhos = self.separar_url(url)

        if dominio not in self.__dominios:
            self.__dominios[dominio] = NoPagina()

        atual = self.__dominios[dominio]
        for caminho in caminhos:
            atual = atual.filhos.setdefault(caminho, NoPagina())

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
        return ["/" + nome for nome in sorted(pagina.filhos)]

    def obter_arquivo(self, url):
        pagina = self.buscar(url)
        return None if pagina is None else pagina.arquivo

    def listar_dominios(self):
        return sorted(self.__dominios)
