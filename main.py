from cadastro_urls import CadastroURLs
from navegador import Navegador

def exibir_interface(navegador):
    hist_str = navegador.obter_historico_formatado()
    home_str = f"[{navegador.pagina_atual}]" if navegador.pagina_atual else "[]"
    
    print("-" * 50)
    print(f"Histórico de Visitas: {hist_str if hist_str else '[]'}")
    print(f"Home: {home_str}")
    print("Digite a url ou #back para retornar à última página visitada.")

def main():
    cadastro = CadastroURLs()
    cadastro.carregar_arquivo("urls.txt")
    navegador = Navegador(cadastro)

    mensagem_status = None

    while True:
        exibir_interface(navegador)
        
        if mensagem_status:
            print()
            print(mensagem_status)
            mensagem_status = None

        entrada = input("url: ").strip()

        if entrada == "":
            continue

        if entrada == "#sair":
            print("Encerrando o navegador...")
            break

        elif entrada == "#back":
            pagina = navegador.voltar()
            if pagina is None:
                mensagem_status = "Não há páginas anteriores no histórico."

        elif entrada == "#showhist":
            hist = navegador.obter_historico_formatado()
            print(f"\nHistórico: {hist if hist else '[]'}\n")

        elif entrada.startswith("#add"):
            nova_url = entrada[4:].strip()
            if nova_url == "":
                mensagem_status = "Erro: Use o formato #add <url>"
            else:
                try:
                    cadastro.adicionar(nova_url)
                    mensagem_status = f"URL '{nova_url}' cadastrada com sucesso!"
                except ValueError as erro:
                    mensagem_status = f"Erro ao cadastrar: {erro}"

        elif entrada.startswith("#"):
            mensagem_status = "Comando desconhecido."

        else:
            try:
                navegador.acessar(entrada)
                mensagem_status = "Página encontrada!"
            except ValueError as erro:
                mensagem_status = str(erro)

if __name__ == "__main__":
    main()