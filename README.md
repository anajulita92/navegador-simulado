# Navegador Simulado — Checkpoint 2

Projeto acadêmico em Python para simular a navegação entre domínios e páginas internas. O programa não realiza requisições HTTP reais: cada página é representada por um arquivo de texto local.

## Requisitos

- Python 3.9 ou superior.
- Nenhuma biblioteca externa.

## Como executar

Na pasta do projeto:

```bash
python main.py
```

## Comandos

| Comando | Função |
|---|---|
| `#add <url>` | Cadastra um domínio ou página interna e solicita seu conteúdo |
| `#back` | Retorna à página visitada anteriormente |
| `#showhist` | Exibe o histórico |
| `#help` | Exibe a ajuda dos comandos |
| `#sair` | Encerra o programa |

Para navegar, digite um endereço completo cadastrado ou um caminho iniciado por `/`. Exemplo: depois de acessar `www.ifpb.edu.br`, digite `/tsi`; dentro de TSI, digite `/professores`.

## Estrutura do projeto

- `main.py`: interface de terminal e interpretação dos comandos.
- `cadastro_urls.py`: validação, cadastro e persistência.
- `estrutura_web.py`: árvore de domínios e páginas internas.
- `navegador.py`: navegação, leitura e exibição das páginas.
- `historico.py`: pilha encadeada de páginas visitadas.
- `urls.txt`: cadastro inicial de URLs.
- `paginas/`: arquivos `index.txt` associados às URLs.
- `testes/`: testes automatizados.

## Estrutura de dados

A classe `EstruturaWeb` usa uma árvore de dicionários. Cada domínio é uma raiz; cada caminho interno é um nó filho. A busca percorre somente os segmentos informados. Cada página pode apresentar no máximo dois links internos, conforme o modelo do enunciado.

Nós intermediários criados para formar caminhos não são considerados páginas válidas até receberem um arquivo associado.

## Arquivos de conteúdo

Cada URL cadastrada possui um arquivo `index.txt` dentro da pasta `paginas/`. Ao acessar uma URL, o programa exibe o endereço, o conteúdo do arquivo e os links internos cadastrados naquela página.

## Cadastro manual

Digite, por exemplo:

```text
#add www.exemplo.com/contato
```

Depois, informe o conteúdo da página. O programa cria o arquivo local e atualiza `urls.txt`.

## Testes

```bash
python -m unittest discover -s testes -v
```

Os testes cobrem a árvore, o limite de dois links por página, caminhos com acentos, navegação interna, histórico, arquivos e erros 404.
