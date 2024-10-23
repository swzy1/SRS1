import socket
import _thread

clients = []

def client_thread(con, addr):
    print(f"Клиент {addr} подключился")

    while True:
        try:
            data = con.recv(1024)
            if not data:
                break

            message = data.decode()
            print(f"Сообщение от {addr}: {message}")
            for client in clients:
                if client != con:
                    client.send(data)
        except:
            break

    print(f"Клиент {addr} Отключился")
    con.close()
    clients.remove(con)

server = socket.socket()
hostname = socket.gethostname()
port = 12345
server.bind((hostname, port))
server.listen(2)

print("Сервер запущен")
while True:
    con, addr = server.accept()
    clients.append(con)
    _thread.start_new_thread(client_thread, (con, addr))
