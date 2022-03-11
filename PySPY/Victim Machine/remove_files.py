import shutil 

def remove(path):
        shutil.rmtree(path,ignore_errors=True)

if __name__ == '__main__':
        remove()
