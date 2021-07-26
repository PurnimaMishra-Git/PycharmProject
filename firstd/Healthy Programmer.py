# Healthy Programmer
import datetime
from time import time
from pygame import mixer
b=datetime.datetime.now()
watertime=time()
eyetime=time()
acttime=time()
mixer.init()
while True:
   if time()-watertime>60*30:
        mixer.music.load("Party On My Mind.mp3")
        mixer.music.play()
        userinput=input("Press D for stop: ")

        if userinput == "D":
            watertime = time()
            mixer.music.stop()
            with open("waterlog.txt", "a")as f:
              dis = f.write(str(b) + userinput)

   if time()- eyetime>60*45:
        mixer.music.load("Mirrors.mp3")
        mixer.music.play()
        userinput=input("Press E for stop: ")
        if userinput == "E":
         eyetime = time()
         mixer.music.stop()
        with open("eyelog.txt", "a")as f:
            dis = f.write(str(b) + userinput)


   if time()-acttime>60*60:
        mixer.music.load("One Time.mp3")
        mixer.music.play()
        userinput=input("Press A for stop: ")
        if userinput == "A":
         acttime = time()
         mixer.music.stop()
        with open("activitylog.txt", "a")as f:
                dis = f.write(f"{datetime.datetime.now()}\n"+    userinput)





