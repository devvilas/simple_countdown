import time
from datetime import datetime
import os 
import pyfiglet
from datetarget import target

def countdow_timer(target_datetime):
    while True:
        now = datetime.now()
        delta = target_datetime - now
        if delta.total_seconds() <= 0:
            print("Countdown finished!")
            break
        seconds = delta.seconds
        hours = seconds // 3600
        minutes = (seconds % 3600) // 60
        seconds = seconds % 60
        output = (f"{hours:02d} : {minutes:02d} : {seconds:02d}")
        f = pyfiglet.Figlet(font='colossal')
        print(f.renderText(output))
        time.sleep(1)
        os.system("cls")

future_datetime = target
countdow_timer(future_datetime)