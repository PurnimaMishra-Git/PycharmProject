import datetime
import timer
from time import time
from pygame import mixer

watertime=time()
eyetime=time()
actitime=time()

def func_music(file, stop):

    mixer.init()

    mixer.music.set_volume(0.2)
while True:
    mixer.music.load()
    mixer.music.play()
    userinput=input("ENTER INPUT:  ")
    if userinput == "stop":
        mixer.music.stop()
        break

def func_log(file,msg):
    with open("file","a") as f:
     f.write(f"{datetime.now()}  {msg}")

if __name__ == '__main__':

    while True:

          if time() - watertime > 5:
              func_music("Party On My Mind.mp3","D")
              watertime = time()
              func_log("Waterlog2.txt","Drank")
          if time() - eyetime > 20:
              func_music("Mirrors.mp3", "E")
              eyetime = time()
              func_log("eyelog2.txt", "Eye")
          if time() - actitime > 75:
              func_music("One Time.mp3", "A")
              actitime = time()
              func_log("Actlog2.txt", "Activity")

