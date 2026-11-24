from cadastro_urls import CadastroURLs
from navegador import Navegador


def exibir_interface(navegador):
    historico = navegador.obter_historico_formatado()
    pagina = navegador.pagina_atual or "[]"

    print("\n" + "=" * 60)
    print(f"Histórico de Visitas: {historico or '[]'}")
    print(f"Home: [{pagina}]" if navegador.pagina_atual else "Home: []")
    print("Digite uma URL, um caminho interno iniciado por / ou um comando #.")
    print("=" * 60)


def exibir_ajuda():
    print("""
COMANDOS DO NAVEGADOR SIMULADO

  #add <url>     Cadastra um domínio ou uma página interna.
                 Depois, informe o conteúdo que ficará no arquivo .txt.
  #back          Retorna à página visitada imediatamente antes.
  #showhist      Exibe o histórico de páginas visitadas.
  #help          Exibe esta ajuda.
  #sair          Encerra o navegador.

NAVEGAÇÃO

  www.ifpb.edu.br       Acessa um domínio cadastrado.
  /tsi                  Acessa um link interno da página atual.
  /professores          A partir de /tsi, acessa /tsi/professores.

Digite somente links internos que estejam listados na página atual.
""")


def main():
    cadastro = CadastroURLs()
    try:
        cadastro.carregar_arquivo("urls.txt")
    except OSError as erro:
        print(f"Não foi possível carregar o cadastro inicial: {erro}")
        return

    navegador = Navegador(cadastro)

    print("NAVEGADOR SIMULADO - CHECKPOINT 2")
    print("Digite #help para consultar os comandos.")

    while True:
        exibir_interface(navegador)

        try:
            entrada = input("url: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\nEncerrando o navegador...")
            break

        if not entrada:
            continue

        if entrada == "#sair":
            print("Encerrando o navegador...")
            break
        if entrada == "#help":
            exibir_ajuda()
            continue
        if entrada == "#showhist":
            print("Histórico:", navegador.obter_historico_formatado() or "[]")
            continue
        if entrada == "#back":
            anterior = navegador.voltar()
            if anterior is None:
                print("Não há páginas anteriores no histórico.")
            else:
                navegador.exibir_pagina_atual()
            continue

        if entrada == "#add" or entrada.startswith("#add "):
            endereco = entrada[4:].strip()
            if not endereco:
                print("Uso: #add <url>")
                continue
            try:
                conteudo = input("Conteúdo da nova página: ")
                pagina = cadastro.adicionar(endereco, conteudo)
                print(f"Página cadastrada com sucesso: {pagina}")
            except (ValueError, OSError) as erro:
                print(f"Erro ao cadastrar: {erro}")
            continue

        if entrada.startswith("#"):
            print("Comando desconhecido. Digite #help para ver os comandos.")
            continue

        try:
            pagina = navegador.acessar(entrada)
            print(f"Página encontrada: {pagina}")
            navegador.exibir_pagina_atual()
        except (ValueError, OSError) as erro:
            print(erro)


if __name__ == "__main__":
    main()
