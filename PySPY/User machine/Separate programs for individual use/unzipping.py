# importing required modules
from zipfile import ZipFile

# specifying the zip file path
file_name = "+EDIT [ex-S:\Folder_name\zipped.zip]+"

# path where the file will be unzipped
#if doesnt work make a new folder and add its path
extraction_path="+EDIT [ex-S:\Folder_name\extraction_folder]+"

# opening the zip file in READ mode
with ZipFile(file_name, 'r') as zip:
    
    # printing all the contents of the zip file
    zip.printdir()

    # extracting all the files
    print('Extracting all the files now...')
    zip.extractall(extraction_path)
    print('Done!')