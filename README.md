# socket-attack

Este repositório contém dois exemplos de scripts em Python que simulam um cenário de comunicação entre uma Vítima e um Atacante usando a biblioteca `socket` e `subprocess`. O servidor atua como a Vítima e o cliente como o Atacante, enviando comandos e recebendo dados do servidor.

# Estrutura do Projeto

- `server.py`: Script que representa o servidor (Vítima), escuta conexões, executa comandos e envia arquivos.
- `client.py`: Script que representa o cliente (Atacante), conecta-se ao servidor, envia comandos e solicita arquivos.

# Como Executar

1. Execute o `server.py` para iniciar o servidor (vítima).
2. Execute o `client.py` para iniciar o cliente (atacante) e conectar-se ao servidor.

# Pré-requisitos

- Python 3.x instalado.
- Bibliotecas: socket e subprocess (padrões do Python)

# Instalação

git clone https://github.com/FelipeMendoncaaa/socket-attack.git
cd socket-attack
