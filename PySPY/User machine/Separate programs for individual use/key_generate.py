from cryptography.fernet import Fernet
import os

def key_gen():
    path=os.getcwd()                                    #get path 
    key=Fernet.generate_key()                           #generate key for encryption
    key_file=open(path+"\\encryption_key.txt",'wb')     #storing in separate file
    
    print("==========} \t KEY created \t {==========")
    print(f"\nKey  ::>  {key}")
    print(f"\nPath ::>  {path}\n")          
    key_file.write(key)
    key_file.close()

if __name__ == "__main__":
    key_gen()