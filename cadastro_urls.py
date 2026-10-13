class CadastroURLs:
    def __init__(self):
        self.__urls = []

    def esta_cadastrada(self, url):
        return url in self.__urls

    def validar_url(self, url):
        # O endereço precisa ser texto e não pode estar vazio
        if not isinstance(url, str):
            raise ValueError("A URL deve ser texto.")

        if url == "":
            raise ValueError("A URL não pode estar vazia.")

        for caractere in url:
            if caractere.isspace():
                raise ValueError("A URL não pode conter espaços.")

        # Analisa o endereço sem mudar a URL original
        endereco = url

        # Retira o protocolo, se tiver
        if url[:7] == "http://":
            endereco = url[7:]
        elif url[:8] == "https://":
            endereco = url[8:]

        # Nesta versão, não usamos parâmetros ou fragmentos
        if "?" in endereco or "#" in endereco:
            raise ValueError("Não usamos parâmetros ou fragmentos nesta versão.")

        dominio = endereco.split("/")[0]
        partes = dominio.split(".")

        if len(partes) < 2:
            raise ValueError("O domínio deve ter partes separadas por ponto.")

        for parte in partes:
            # Recusa casos como www..exemplo.com
            if parte == "":
                raise ValueError("O domínio não pode ter partes vazias.")

            # O hífen pode ficar no meio, mas não nas pontas
            if parte[0] == "-" or parte[-1] == "-":
                raise ValueError("Uma parte do domínio não pode começar ou terminar com hífen.")

            for caractere in parte:
                if not (caractere.isascii() and caractere.isalnum()) and caractere != "-":
                    raise ValueError("O domínio deve conter apenas letras, números e hífen.")

        return True

    def separar_endereco(self, url):
        protocolo = ""
        endereco = url

        if url[:7] == "http://":
            protocolo = "http://"
            endereco = url[7:]
        elif url[:8] == "https://":
            protocolo = "https://"
            endereco = url[8:]

        # Compara os domínios sem diferenciar maiúsculas e minúsculas
        dominio = endereco.split("/")[0].lower()
        return protocolo, dominio

    def adicionar(self, url):
        self.validar_url(url)

        if self.esta_cadastrada(url):
            raise ValueError("A URL já está cadastrada.")

        protocolo, dominio = self.separar_endereco(url)

        # Mantém o mesmo formato de protocolo para as páginas de um domínio
        for cadastrada in self.__urls:
            protocolo_existente, dominio_existente = self.separar_endereco(cadastrada)

            if dominio == dominio_existente and protocolo != protocolo_existente:
                raise ValueError("Esse domínio já está cadastrado com outro formato de protocolo.")

        self.__urls.append(url)

    def carregar_arquivo(self, caminho):
        # Trata problemas ao abrir ou ler o arquivo
        try:
            with open(caminho, "r", encoding="utf-8") as arquivo:
                for numero, linha in enumerate(arquivo, start=1):
                    url = linha.strip()

                    # Ignora linhas vazias
                    if url != "":
                        try:
                            self.adicionar(url)
                        except ValueError as erro:
                            print(f"Linha {numero} ignorada: {erro}")

        except OSError as erro:
            print(f"Não foi possível ler o arquivo: {erro}")

        except UnicodeError:
            print("Não foi possível ler o texto. Salve o arquivo em UTF-8.")


# Executa o teste apenas quando este arquivo é iniciado diretamente
if __name__ == "__main__":
    cadastro = CadastroURLs()
    cadastro.carregar_arquivo("urls.txt")

    print(cadastro.esta_cadastrada("https://www.python.org"))
    print(cadastro.esta_cadastrada("https://www.wikipedia.org"))