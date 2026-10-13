# Navegador Simulado

## Como executar

É necessário ter o Python 3 instalado no computador.

1. Clone o repositório ou baixe o ZIP e extraia os arquivos.
2. Abra o terminal na pasta do projeto.
3. Execute o comando:

    python3 main.py

O arquivo urls.txt deve estar na mesma pasta do main.py. Depois de iniciar, digite uma URL cadastrada ou um dos comandos disponíveis.

## Arquivos do projeto

- main.py: recebe as entradas do usuário e executa os comandos.
- cadastro_urls.py: valida, cadastra e carrega as URLs do arquivo.
- historico.py: implementa a pilha usada para guardar as páginas anteriores.
- navegador.py: controla a página atual, os acessos e o retorno.
- urls.txt: contém os endereços iniciais, um por linha.

## Comandos disponíveis

- Digitar uma URL: acessa o endereço, se estiver cadastrado.
- #add <url>: cadastra um novo endereço.
- #back: volta à página anterior.
- #showhist: mostra a página atual e o histórico, do mais recente para o mais antigo.
- #sair: encerra o programa.


## Funcionamento e limitações

- O programa simula a navegação, sem acessar sites reais. Os endereços iniciais são lidos do arquivo urls.txt.
- O histórico usa uma pilha: a última página guardada é a primeira recuperada ao voltar. Acessos inválidos não alteram a página atual nem o histórico.
- A consulta usa o endereço exato. Novos cadastros ficam disponíveis somente durante a execução e não são salvos no arquivo.
- As páginas de um mesmo domínio devem usar o mesmo protocolo, ou todas ficar sem protocolo. URLs com parâmetros (?) ou fragmentos (#) não são aceitas.


## Testes realizados

- Leitura das URLs do arquivo, incluindo linhas vazias, endereços inválidos e repetidos.
- Tratamento de arquivo inexistente.
- Cadastro de URLs e recusa de duplicatas ou protocolos diferentes para o mesmo domínio.
- Acesso a páginas cadastradas e tentativa de acesso a endereços inválidos ou não cadastrados.
- Consulta do histórico e retorno à página anterior, inclusive com histórico vazio.
- Entrada vazia, comando desconhecido, uso de #add sem endereço e encerramento com #sair.