# Navegador Simulado — Checkpoint 2

Projeto acadêmico em Python para simular a navegação entre domínios e páginas internas, sem realizar requisições HTTP reais.

## Requisitos

- Python 3.9 ou superior.
- Nenhuma biblioteca externa é necessária.

## Como executar

Na pasta do projeto, execute:

```bash
python main.py
```

O programa carrega os domínios de `urls.txt` e lê o conteúdo das páginas nos arquivos `.txt` dentro de `paginas/`.

## Comandos

| Comando | Função |
|---|---|
| endereço completo | Acessa um domínio ou página cadastrada |
| `/caminho` | Acessa uma página interna a partir da página atual |
| `#add <endereço>` | Cadastra um domínio ou página e solicita o conteúdo |
| `#back` | Retorna à página anterior |
| `#showhist` | Exibe o histórico |
| `#help` | Exibe a ajuda |
| `#sair` | Encerra o programa |

## Estrutura dos arquivos

- `main.py`: interface de terminal e interpretação dos comandos.
- `cadastro_urls.py`: validação, cadastro e persistência dos endereços.
- `estrutura_web.py`: árvore de domínios e páginas internas.
- `navegador.py`: navegação, resolução de caminhos, leitura e exibição das páginas.
- `historico.py`: pilha encadeada de páginas visitadas.
- `urls.txt`: lista de domínios e páginas iniciais.
- `paginas/`: conteúdo das páginas, um arquivo `index.txt` por endereço.
- `testes/`: testes automatizados.

## Como funciona a navegação interna

Depois de acessar `www.ifpb.edu.br`, digite `/cursos`. O navegador resolve o caminho para `www.ifpb.edu.br/cursos`. A partir dessa página, `/redes` resolve para `www.ifpb.edu.br/cursos/redes`.

Os caminhos são acrescentados ao caminho da página atual. O comando `#back` retorna à página anterior.

## Cadastro de páginas

Use `#add www.exemplo.com/secao`. O programa solicita o texto da página, cria o arquivo correspondente dentro de `paginas/` e atualiza `urls.txt`. Os cadastros permanecem salvos para as próximas execuções.

## Testes

Execute:

```bash
python -m unittest discover -s testes -v
```

Os testes verificam o acesso ao domínio, navegação interna, leitura de arquivo, erro 404 sem alteração do estado e retorno pelo histórico.

## Observações

O projeto é um navegador simulado. Ele não acessa a internet nem interpreta HTML; cada página é representada por um arquivo de texto local.
