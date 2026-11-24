from cadastro_urls import CadastroURLs
from navegador import Navegador


def exibir_interface(navegador):
    historico = navegador.obter_historico_formatado()
    pagina = navegador.pagina_atual or "Nenhuma página acessada"

    print("\n" + "=" * 60)
    print(f"Histórico de visitas: {historico or '[]'}")
    print(f"Página atual: {pagina}")
    print("=" * 60)


def exibir_ajuda():
    print("""
COMANDOS DO NAVEGADOR SIMULADO

  endereço completo       Acessa um domínio ou página cadastrada.
  /caminho                Acessa uma página interna do domínio atual.
  #add <endereço>         Cadastra um domínio ou página interna.
  #back                   Volta à página anterior.
  #showhist               Exibe o histórico de navegação.
  #help                   Exibe esta ajuda.
  #sair                   Encerra o navegador.

Exemplo:
  www.ifpb.edu.br
  /cursos
  /redes
""")


def main():
    cadastro = CadastroURLs()
    cadastro.carregar_arquivo("urls.txt")
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
                print(f"Retornou para: {anterior}")
                navegador.exibir_pagina_atual()
            continue

        if entrada.startswith("#add"):
            endereco = entrada[4:].strip()
            if not endereco:
                print("Uso: #add <endereço>")
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
