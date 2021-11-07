import pygame.mixer as player
from time import strftime, sleep
import argparse

parser = argparse.ArgumentParser("Play hourly music from a given Animal Crossing game.")
parser.add_argument("-pg",help="Play music from Population Growing (aka GameCube)",action="store_true")
parser.add_argument("-ww",help="Play music from Wild World",action="store_true")
parser.add_argument("-cf",help="Play music from City Folk",action="store_true")
parser.add_argument("-nl",help="Play music from New Leaf",action="store_true")
parser.add_argument("-nh",help="Play music from New Horizons",action="store_true")
options = parser.parse_args()

player.init()
player.music.set_volume(1.0)
def mainLoop(pg,ww,cf,nl,nh):
    tim = strftime("%H")
    if tim != last_tim:
        if pg:
            player.music.load("./Music/Population_Growing/{}.mp3".format(str(tim)))
        else if ww:
            player.music.load("./Music/Wild_World/{}.mp3".format(str(tim)))
        else if cf:
            player.music.load("./Music/City_Folk/{}.mp3".format(str(tim)))
        else if nl:
            player.music.load("./Music/New_Leaf/{}.mp3".format(str(tim)))
        else if nh:
            player.music.load("./Music/New_Horizons/{}.mp3".format(str(tim)))
        player.music.play(loops=-1)
        sleep(10)
    last_tim=tim

while True:
    mainLoop(**vars(options))


