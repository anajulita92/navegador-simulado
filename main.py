from cadastro_urls import CadastroURLs
from navegador import Navegador


cadastro = CadastroURLs()
cadastro.carregar_arquivo("urls.txt")
navegador = Navegador(cadastro)

print("Navegador simulado")
print("Digite uma URL para acessar.")
print("Comandos: #add <url>, #back, #showhist e #sair")

while True:
    print()
    print("Página atual:", navegador.pagina_atual)
    entrada = input("URL ou comando: ").strip()

    try:
        if entrada == "":
            print("Digite uma URL ou um comando.")

        elif entrada == "#sair":
            print("Programa encerrado.")
            break

        elif entrada == "#back":
            pagina = navegador.voltar()

            if pagina is None:
                print("Não há página anterior.")
            else:
                print("Retornou para:", pagina)

        elif entrada == "#showhist":
            print("Página atual:", navegador.pagina_atual)
            historico = navegador.listar_historico()

            if len(historico) == 0:
                print("Histórico vazio.")
            else:
                print("Histórico, do mais recente para o mais antigo:")
                for url in historico:
                    print(url)

        elif entrada == "#add" or entrada[:5] == "#add ":
            url = entrada[4:].strip()

            if url == "":
                print("Use: #add <url>")
            else:
                cadastro.adicionar(url)
                print("URL cadastrada.")

        elif entrada[0] == "#":
            print("Comando desconhecido.")

        else:
            navegador.acessar(entrada)
            print("Página encontrada!")

    except ValueError as erro:
        print(f"Erro: {erro}")