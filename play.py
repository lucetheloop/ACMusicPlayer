import pygame.mixer as player
from time import strftime, sleep
import argparse

parser = argparse.ArgumentParser("Play hourly music from a given Animal Crossing game.")
parser.add_argument("-pg",help="Play music from Population Growing (aka GameCube)",action="store_true")
parser.add_argument("-ww",help="Play music from Wild World",action="store_true")
parser.add_argument("-cf",help="Play music from City Folk",action="store_true")
parser.add_argument("-nl",help="Play music from New Leaf",action="store_true")
parser.add_argument("-nh",help="Play music from New Horizons",action="store_true")
parser.add_argument("--vol",type=float, default=1, help="Change volume")
options = parser.parse_args()

player.init()

def mainLoop(pg,ww,cf,nl,nh,vol):
    last_tim=-1
    player.music.set_volume(vol)
    while True:
        tim = strftime("%H")
        if tim != last_tim:
            if pg:
                player.music.load("./Music/Population_Growing/{}.mp3".format(str(tim)))
            elif ww:
                player.music.load("./Music/Wild_World/{}.mp3".format(str(tim)))
            elif cf:
                player.music.load("./Music/City_Folk/{}.mp3".format(str(tim)))
            elif nl:
                player.music.load("./Music/New_Leaf/{}.mp3".format(str(tim)))
            elif nh:
                player.music.load("./Music/New_Horizons/{}.mp3".format(str(tim)))
            player.music.play(loops=-1)
            sleep(1)
        last_tim=tim

while True:
    mainLoop(**vars(options))


