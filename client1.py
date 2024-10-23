import socket
import _thread

def receive_messages(client):
    while True:
        data = client.recv(1024)
        if not data:
            break
        print("Вам новое сообщение: ", data.decode())

client = socket.socket()
hostname = socket.gethostname()
port = 12345
client.connect((hostname, port))

_thread.start_new_thread(receive_messages, (client,))

print("Вы можете начать писать сообщения.\nНапишите 'exit', чтобы выйти.")

while True:
    message = input()
    if message.lower() == "exit":
        break
    client.send(message.encode())

client.close()