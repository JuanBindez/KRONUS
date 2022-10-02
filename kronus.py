import os
import time
from datetime import datetime


def loop_time():
    while 1 < 2:
        now = datetime.now()
        tempo = now.strftime("%H:%M")
        print(tempo)
        time.sleep(1)
        
        if tempo == "22:35":
            print("travou!!")
            break
            
        else:
            pass
        
        os.system("clear")
        
        
        
if __name__ == "__main__":
    loop_time()
