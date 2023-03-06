import os


print(os.getcwd())
while 1:
    entry = input("= ")
    
    os.chdir(entry)
    print(os.getcwd())