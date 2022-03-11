from zipfile import ZipFile as zz
import os

def zipper(path,zf): #function to get all files from directory
    file_list=os.listdir(path) 
    for file in file_list:
        with zz(path+zf,'a') as z:
            z.write(path+file)


if __name__=="__main__":
    zipper()