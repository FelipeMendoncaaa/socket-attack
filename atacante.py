import socket

ip = "127.0.0.1"
porta = 51230

ojb_con = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ojb_con.connect((ip, porta))

msg_enviada = bytes("ls", encoding="latin-1")
ojb_con.send(msg_enviada)

msg_recebido = ojb_con.recv(1024).decode(encoding="latin-1")
print("Recebido: ", msg_recebido)

msg_enviada = bytes(input("Entre com o Nome do Arquivo: "), encoding="latin-1")
ojb_con.send(msg_enviada)

dados = ojb_con.recv(1024000)
with open("fiap.png", "wb") as file:
    file.write(dados)