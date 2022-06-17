# Healthy Programmer

from pygame import mixer
from datetime import datetime
from time import time

def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a = input()
        if a == stopper:
            mixer.music.stop()
            break

def log(msg):
    with open("log_file.txt", "a") as f:
        f.write(f"{msg}{datetime.now()}\n")
if __name__ == '__main__':
    water_timer = time()
    eye_timer = time()
    exercise_timer = time()
    water_delay = 40*60
    eye_delay = 45*60
    exercise_delay = 30*60

    while True:
        if time() - water_timer > water_delay:
            print("It's water drinking time. Enter drank to stop music")
            musiconloop("After_dark.mp3", "drank")
            water_timer = time()
            log("Drank water at ")
        if time() - eye_timer > eye_delay:
            print("It's time to do some eyes exercise. Enter done to stop music")
            musiconloop("After_dark.mp3", "done")
            eye_timer = time()
            log("Eyes relaxed at")
        if time() - exercise_timer > exercise_delay:
            print("It's to do some physical exercise. Enter done to stop music")
            
            musiconloop("After_dark.mp3", "done")
            exercise_timer = time()
            log("Physical activity at ")