from cryptography.fernet import Fernet
import threading
import zipfile
import os
import time

## do not touch these unless uk what ur trying to do
txt_tup=()                                              # tuple for storing txt file name
png_tup=()                                              # tuple for storing png file name
audio=""                                                # variable for storing audio file name


def choice():
      i=0
      while i!=5:
            os.system("cls")
            print("====="*10+" SCRIPT FOR USER of PYSPY "+"====="*10)
            print("\n Options :"+
            "\n\t 1.Generate Encryption Key"+
            "\n\t 2.To Get ZIP Info"+
            "\n\t 3.UNZIP File"+
            "\n\t 4.Decrypt File"+
            "\n\t 5:EXIT"
            "\n")

            try:
                  i=int(input("Enter Choice:"))
            except Exception as e:
                  print("Wrong Input !!!")
                  time.sleep(2)
                  choice()

            ch = {
                  1:gen_key,
                  2:zipinfo,
                  3:unzip,
                  4:decrypt,
                  5:end
                  }
            if (i>=1 and i<=5):
                  ch.get(i)()
            else:
                  print("Enter number from 1-5")
                  time.sleep(2)

def gen_key():
      path=os.getcwd()                                    #get path 
      key=Fernet.generate_key()                           #generate key for encryption
      key_file=open(path+"\\encryption_key.txt",'wb')     #storing in separate file
      
      print("==========} \t KEY created \t {==========")
      print(f"\nKey  ::>  {key}")
      print(f"\nPath ::>  {path}\n")          
      key_file.write(key)
      key_file.close()
      end()

def zipinfo():
      
      path=input("\n=} Enter Zip File Path : ")

      def main():      
            if path.endswith(".zip"):
                  if os.path.exists(path):              #check for valid path
                        zip_details()
                        print("\n\n")
                        end()
                  else:
                        print("\npath doesnt exist !!")
                        print("check [path] and [file name] ,if they are correct ;)")
                        print("Path u entered ::>   "+path)
                        time.sleep(7)
                        zipinfo()
            else:
                  print("\nwrong file, no extension [.zip] present")
                  print("Path u entered ::>   "+path)
                  time.sleep(5)
                  choice()

      def zip_details():
            os.system("cls")            
            print("=======>\t ZIP FILE DETAILS \t<======= \n\n")

            with zipfile.ZipFile(path,'r')as zf:
                  print("---->\t ZIP FILE object ")
                  print(zf)
                  print("\n---->\t ZIP FILE LIST ")
                  f_list=zf.namelist()                                    #list of files in the zip file
                  for i in f_list:
                        print(f"+> {i}")

                  print("\n\tFor Additional Details of each file enter :"+ 
                        "\n\t    +No  [n]"+
                        "\n\t    +Yes View in console [y]"+
                        "\n\t    +save in a txt file [s]")

                  s=input("\n\n\tEnter choice : ")

                  if s=='y':        
                        print("\n---->\t EACH FILE DETAIL\n")
                        print(zf.infolist())
                        time.sleep(3)
                        for z in zf.infolist():                                 #to print details of each file in zip
                              print_zipinfo_details(z)
                  
                  elif s=='s':
                        save_zipinfo(zf)

                  elif s=='n':
                        o=0
                        print("\n\n=> 1.Main Menu")
                        print("=> 2.EXIT\n")

                        try:
                              o=int(input("\tEnter Choice:"))
                        except Exception as e:
                              print("Wrong Input !!!")
                              time.sleep(2)
                              zip_details()

                        if(o==2):
                              print("\n")      
                              time.sleep(1) 
                              end()
                        elif(o==1):
                              time.sleep(1) 
                              choice()
                        else:
                              time.sleep(1)
                              print("Enter 1 or 2 !!")
                              zip_details()

                  else:
                        print("\nWrong Input enter y/n/s")
                        time.sleep(2)
                        zip_details()

      #details of files in the zip
      def print_zipinfo_details(zipinfo):
            print("\n=============== {} ==================".format(zipinfo.filename))
            print("\nLast Modification Datetime of file   : ", zipinfo.date_time)
            print("Compression Type                     : ", zipinfo.compress_type)
            print("Compressed Data Size                 : ", zipinfo.compress_size)
            print("Uncompressed Data Size               : ", zipinfo.file_size)
            print("Comment for file                     : ", zipinfo.comment)
            print("System that created zip file         : ", zipinfo.create_system)
            print("PKZIP Version                        : ", zipinfo.create_version)
            print("PKZIP Version needed for extraction  : ", zipinfo.extract_version)
            print("ZIP Flags                            : ", zipinfo.flag_bits)
            print("Volume Number of File Header         : ", zipinfo.volume)
            print("Internal Attributes                  : ", zipinfo.internal_attr)
            print("External Attributes                  : ", zipinfo.external_attr)
            print("Byte offset to File Header           : ", zipinfo.header_offset)
            print("CRC-32 of compressed data            : ", zipinfo.CRC)
            print("Is zip member directory ?            : ", zipinfo.is_dir())

      def save_zipinfo(zipobj):
            path=os.getcwd()
            print("\n\t===== SAVE ZIP INFO =====\n")
            print("=+ File name : zip-info.txt")
            print("=+ Path where created: "+path+"\\zip-info.txt")
            
            with open(path+"\\zip-info.txt", 'a') as f:                        
                  
                  f.write(f"---->\t ZIP FILE object \n")
                  f.write(f"\n{zipobj}\n")
                  
                  f.write(f"\n---->\t ZIP FILE LIST \n")
                  f_list=zipobj.namelist()                                    #list of files in the zip file
                  for i in f_list:
                        f.write(f"+> {i}\n")            

                  f.write(f"\n\n---->\t EACH FILE DETAIL\n")

                  for z in zipobj.infolist():      
                        f.write(f"\n=============== {z.filename} ==================")
                        f.write(f"\nLast Modification Datetime of file   : {z.date_time}")
                        f.write(f"\nCompression Type                     : {z.compress_type}")
                        f.write(f"\nCompressed Data Size                 : {z.compress_size}")
                        f.write(f"\nUncompressed Data Size               : {z.file_size}")
                        f.write(f"\nComment for file                     : {z.comment}")
                        f.write(f"\nSystem that created zip file         : {z.create_system}")
                        f.write(f"\nPKZIP Version                        : {z.create_version}")
                        f.write(f"\nPKZIP Version needed for extraction  : {z.extract_version}")
                        f.write(f"\nZIP Flags                            : {z.flag_bits}")
                        f.write(f"\nVolume Number of File Header         : {z.volume}")
                        f.write(f"\nInternal Attributes                  : {z.internal_attr}")
                        f.write(f"\nExternal Attributes                  : {z.external_attr}")
                        f.write(f"\nByte offset to File Header           : {z.header_offset}")
                        f.write(f"\nCRC-32 of compressed data            : {z.CRC}")
                        f.write(f"\nIs zip member directory ?            : {z.is_dir}")
                        f.write(f"\n")

      main()

def unzip():
      os.system("cls")
      print("==========} \t UNZIP \t {==========\n\n")
      path=input("=} Enter Zip File Path : ")
      
      if path.endswith(".zip"):
            if os.path.exists(path):              #check for valid path
                  pass
            else:
                  print("\npath doesnt exist !!")
                  print("check [path] and [file name] ,if they are correct ;)")
                  print("Path u entered ::>   "+path)
                  time.sleep(7)
                  unzip()
      else:
            print("\nwrong file, no extension [.zip] present")
            print("Path u entered ::>   "+path)
            time.sleep(5)
            choice()

      # path where the file will be unzipped
      extraction_path=input("\n=} Enter Path where u want it to be Extracted:")
      if os.path.exists(extraction_path):              #check for valid path
            pass
      else:
            print("\nExtraction path doesnt exist !!")
            print("check [path] if its correct ;)")
            print("Extraction Path u entered ::>   "+extraction_path)
            time.sleep(7)
            unzip()

      # opening the zip file in READ mode
      with zipfile.ZipFile(path, 'r') as zip:
      
            # extracting all the files
            print('\n\n\t =+=> Extracting all the files now...\n\n')

            # printing all the contents of the zip file
            zip.printdir()
            
            zip.extractall(extraction_path)
            
            print('Done!')
            print("\n\n\t-) if it doesnt work make a new folder and add its path for [extraction_path] (-\n")
            end()

def decrypt(): 

      os.system("cls")            
      print("=======>\t DECRYPTION \t<======= \n\n")

      ##file paths for accessing location
      path = input("=} Enter path of folder containing the encrypted files : ")         # Enter the file path you want your files to be saved to
      path+="\\"

      ##key
      key=input("\n=} Enter Key for decryption : ")
            # encryption key
      
      def main():

            print("decrypting ...... \n")
            print("KEY ::> "+key)
            print("FILE PATH ::> "+path+"\n")

            e_key=Fernet(key)                                     #assigning key for decrypting

            def get_files():                                      #function to get all files from the folder
                  
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

      if os.path.exists(path):
            main()
            print("\t >>if files arent decrypted check key entered <<")
            time.sleep(1)
            print("\n\n \t\t !!! done !!!")
            time.sleep(3)
            end() 
      else:
            print("[path] doesnt exist, check path and folder name")
            time.sleep(3)
            choice()

def end():
      print("========= >>> CLOSEd <<< =========")
      exit()



if __name__ == "__main__":
      
      choice()

