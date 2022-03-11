
from cryptography.fernet import Fernet
import threading
import os

##file paths for accessing location [add double \\ to be safer]
path = "+EDIT [ex-S:\\foldername\\folder having encrypted data]+"          # Enter the file path you want your files to be saved to
path+="\\"

##key in double quotes[ex-"g5HerbAODsBWRNiuczyWaejbmse41thVkyCQ2PQnIjI="]
key="+EDIT-Enter Encryption key [ex-g5HerbAODsBWRNiuczyWaejbmse41thVkyCQ2PQnIjI=]+"       # encryption key 


## do not touch these unless uk what ur trying to do
txt_tup=()                                              # tuple for storing txt file name
png_tup=()                                              # tuple for storing png file name
audio=""                                                # variable for storing audio file name


def main():

    e_key=Fernet(key)                                   #assigning key for decrypting

    def get_files():                                    #function to get all files from the folder

        global txt_tup
        global png_tup
        global audio

        list=os.listdir(path)                           #list the files in folder 

        for x in list:                                  #for filtering files for faster decryption
            if x.endswith(".txt"):
                txt_tup+=(x,)
            if x.endswith(".png"):
                png_tup+=(x,)
            if x.endswith(".wav"):
                audio=(str)(x)        
    
    def de_txt():                                       # Function for decrypting text
        for tf in txt_tup:
            try:
                with open(path+tf,'rb') as f:
                    data=f.read()
                    decryted_data=e_key.decrypt(data)
                
                with open(path+tf, 'wb')as f:
                    f.write(decryted_data)
                print(tf+" - decrypted")

            except Exception :
                print("==> text files allready decrypted <==")
                break

    def de_png():                                        # Function for decrypting images
        for pf in png_tup:
            try:
                with open(path+pf,'rb') as f:
                    data=f.read()
                    decryted_data=e_key.decrypt(data)
                
                with open(path+pf, 'wb')as f:
                    f.write(decryted_data)
                print(pf+" - decrypted")

            except Exception :
                print("==> image files allready decrypted <==")
                break
                

    def de_wav():                                       # Function for decrypting audio
        try:
            with open(path+audio,'rb') as f:
                    data=f.read()
                    decryted_data=e_key.decrypt(data)
                
            with open(path+audio, 'wb')as f:
                    f.write(decryted_data)
            print(audio+" - decrypted")

        except Exception :
                print("==> Audio file allready decrypted <==")
                

    get_files()

    det_t=threading.Thread(target=de_txt,daemon=True)   # thread for text decryption
    dep_t=threading.Thread(target=de_png,daemon=True)   # thread for image decryption
    dew_t=threading.Thread(target=de_wav,daemon=True)   # thread for audio decryption

    dew_t.start()
    det_t.start()
    dep_t.start()
    
    
    det_t.join()
    dep_t.join()
    dew_t.join()

if __name__ == "__main__":
    
    print("decrypting ...... \n")
    print("KEY ::> "+key)
    print("FILE PATH ::> "+path+"\n")
    if os.path.exists(path):
        main()
    else:
        print("wrong path")
    print("\n\n \t\t !!! done !!!")