# Navegador Simulado (Checkpoint 1)

Projeto desenvolvido para a disciplina de **Programação e Estrutura de Dados** do IFPB (Curso de Redes de Computadores), ministrada pelo Prof. Wallennon Germano.

## Como executar

É necessário ter o Python 3 instalado no computador.

1. Clone o repositório ou baixe o ZIP e extraia os arquivos.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

    python3 main.py

O arquivo `urls.txt` deve estar na mesma pasta do `main.py`. Depois de iniciar, digite uma URL cadastrada ou um dos comandos disponíveis.

## Arquivos do projeto

- `main.py`: interface gráfica/terminal que exibe o estado da navegação (Histórico, Home e entradas) e gerencia o loop principal.
- `cadastro_urls.py`: responsável por carregar o arquivo inicial, validar a sintaxe e cadastrar novas URLs na memória.
- `historico.py`: implementação de uma **Pilha encadeada** usada para armazenar a sequência de páginas visitadas.
- `navegador.py`: controla o estado da página atual (`Home`), realiza acessos a URLs e executa o retorno (`#back`).
- `urls.txt`: banco inicial de endereços de sites cadastrados no sistema.

## Comandos disponíveis

- **Digitar uma URL**: acessa o endereço digitado (caso esteja cadastrado no sistema).
- **`#add <url>`**: cadastra um novo endereço durante a execução.
- **`#back`**: desempilha a última página visitada e retorna a ela.
- **`#showhist`**: exibe o histórico de navegação completo na tela.
- **`#sair`**: encerra a aplicação.

## Funcionamento e Regras (Checkpoint 1)

- **Simulação da Web:** O programa simula as requisições web locais sem realizar chamadas HTTP reais. As URLs válidas são carregadas inicialmente a partir do `urls.txt`.
- **Interface e Exibição:** A tela principal exibe o `Histórico de Visitas: [...]` em ordem cronológica de acesso e a página `Home: [...]` atual, conforme os modelos do projeto.
- **Tratamento de Erros:** Caso uma URL não cadastrada seja digitada, o programa exibe explicitamente o erro HTTP simulado (`Erro 404: Página não encontrada!`) e não altera a página atual nem o histórico de navegação.
- **Pilha de Navegação:** O histórico armazena as páginas anteriores. Ao acessar uma nova URL válida, a página corrente vai para a pilha e a nova assume o valor do `Home`. Ao digitar `#back`, a URL do topo é desempilhada.
- **Flexibilidade de Entrada:** A consulta tolera acessos com ou sem protocolo (`http://` ou `https://`), direcionando para o domínio equivalente.

## Testes realizados

- Leitura e povoamento automático das URLs a partir de `urls.txt`.
- Tentativa de acesso a páginas cadastradas e exibição de `Erro 404: Página não encontrada!` para URLs não cadastradas.
- Empilhamento e desempilhamento do histórico de páginas via `#back`.
- Teste do comando `#add <url>` adicionando endereços dinamicamente.
- Teste com histórico vazio ao iniciar e recusa de comandos inválidos.