#module for taking screenshots
from PIL import ImageGrab
import time

# get screenshots
def screenshot(path,name,no,sleep_time):
    count=1
    while no>0:
        im = ImageGrab.grab()
        im.save(f"{path}{count}-{name}")
        count+=1
        no-=1
        time.sleep(sleep_time)

if __name__=="__main__":
    screenshot()