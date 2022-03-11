import zipfile
import os 

#zip file path
path="+EDIT [ex-S:\Folder_name\zipped.zip]+"

if path.endswith(".zip"):
    if os.path.exists(path):              #check for valid path
        pass
    else:
        print("path doesnt exist !!")
        exit()
else:
    print("wrong path")
    print("Path u entered ::>   "+path)
    exit()

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


print("=======>\t ZIP FILE DETAILS \t<======= \n\n")

with zipfile.ZipFile(path,'r')as zf:
    print("---->\t ZIP FILE object ")
    print(zf)
    print("\n---->\t ZIP FILE LIST ")
    f_list=zf.namelist()                                    #list of files in the zip file
    for i in f_list:
        print(i)  
    print("\n---->\t EACH FILE DETAIL ")
    for z in zf.infolist():                                 #to print details of each file in zip
        print_zipinfo_details(z)

