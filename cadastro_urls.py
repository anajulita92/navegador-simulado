class CadastroURLs:
    def __init__(self):
        self.__urls = []

    def normalizar_url(self, url):
        """Remove protocolo e barra final para permitir busca simples/flexível."""
        u = url.strip()
        if u.startswith("http://"):
            u = u[7:]
        elif u.startswith("https://"):
            u = u[8:]
        return u.rstrip("/")

    def esta_cadastrada(self, url):
        norm_busca = self.normalizar_url(url)
        for cadastrada in self.__urls:
            if self.normalizar_url(cadastrada) == norm_busca or cadastrada == url:
                return True
        return False

    def validar_url(self, url):
        if not isinstance(url, str):
            raise ValueError("A URL deve ser texto.")

        url_limpa = url.strip()
        if url_limpa == "":
            raise ValueError("A URL não pode estar vazia.")

        for caractere in url_limpa:
            if caractere.isspace():
                raise ValueError("A URL não pode conter espaços.")

        endereco = self.normalizar_url(url_limpa)

        if "?" in endereco or "#" in endereco:
            raise ValueError("Não usamos parâmetros ou fragmentos nesta versão.")

        dominio = endereco.split("/")[0]
        partes = dominio.split(".")

        if len(partes) < 2:
            raise ValueError("O domínio deve ter partes separadas por ponto.")

        for parte in partes:
            if parte == "":
                raise ValueError("O domínio não pode ter partes vazias.")
            if parte[0] == "-" or parte[-1] == "-":
                raise ValueError("Uma parte do domínio não pode começar ou terminar com hífen.")
            for caractere in parte:
                if not (caractere.isascii() and caractere.isalnum()) and caractere != "-":
                    raise ValueError("O domínio deve conter apenas letras e números.")

        return True

    def adicionar(self, url):
        self.validar_url(url)
        if self.esta_cadastrada(url):
            raise ValueError("A URL já está cadastrada.")
        self.__urls.append(url.strip())

    def carregar_arquivo(self, caminho):
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                for numero, linha in enumerate(arquivo, start=1):
                    url = linha.strip()
                    if url != "":
                        try:
                            self.adicionar(url)
                        except ValueError as erro:
                            # Se for aviso de duplicada, apenas ignora sem travar
                            pass
        except OSError as erro:
            print(f"Não foi possível ler o arquivo: {erro}")