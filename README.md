#  Socket Attack 

---

Este repositório contém dois exemplos de scripts em Python que simulam um cenário de comunicação entre uma **Vítima** e um **Atacante**, usando as bibliotecas `socket` e `subprocess`. O **servidor** atua como a **Vítima** e o **cliente** como o **Atacante**, enviando comandos e recebendo dados do servidor.

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![License](https://img.shields.io/badge/License-MIT-yellow.svg)

---

## 📁 Estrutura do Projeto

- **`server.py`**: Representa o **servidor (Vítima)**, que escuta conexões, executa comandos e envia arquivos ao cliente.
- **`client.py`**: Representa o **cliente (Atacante)**, que conecta-se ao servidor, envia comandos e solicita arquivos.

---

## 🛠️ Pré-requisitos

- Python 3.x instalado (Verifique executando `python --version`).
- As bibliotecas **socket** e **subprocess** são nativas do Python, portanto, não é necessário instalar pacotes adicionais.

---

## 💻 Instalação

1. Clone o repositório para sua máquina local:
   ```bash
   git clone https://github.com/FelipeMendoncaaa/socket-attack.git

2. Navegue até o diretório do projeto:
   ```bash
   cd socket-attack

---

## 🚀 Como Executar

1. No **terminal 1**, execute o script do servidor:
   ```bash
   python3 server.py

2. No **terminal 2**, execute o script do cliente:
   ```bash
   python3 atacante.py

---

## 📜 Licença

- Distribuído sob a licença **MIT**. Veja o arquivo **LICENSE** para mais informações.

---
