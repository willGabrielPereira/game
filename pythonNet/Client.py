import socket

servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(("", 6565))
while True:
    mensagem_byte, ip_client = servidor.recvfrom(2048)
    mensagem = mensagem_byte.decode().lower()
