import socket

PORT = 8888
IP = '127.0.0.1'

print("Server Started !!")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((IP, PORT))

print("Waitng for connexion")

s.listen(5)

client, address = s.accept()

print(f"{address} connected")


while 1:

        text = input( "= ")
        if text == "exit":
            break

        client.sendall(text.encode())
          
        response = client.recv(1024)
        if response != "":
                print(response.decode())
        


print("CLOSE")
client.close()