""" This program formats the music filenames into a form that can be parsed by the main program. """

import os,sys

masterdir = sys.argv[1]
files = os.listdir(masterdir)
print(masterdir)
print(files)
for i in files:
    try:
        if "PM" in i:
            os.rename(masterdir+i,[masterdir+str(int(s)+12)+".mp3" for s in i.replace("PM","").split() if s.isdigit()][0])
        else:
            os.rename(masterdir+i,[masterdir+s+".mp3" for s in i.replace("AM","").split() if s.isdigit()][0])
        
    except IndexError:
        pass
os.rename(masterdir+"12.mp3",masterdir+"24.mp3.temp")
os.rename(masterdir+"24.mp3",masterdir+"12.mp3")
os.rename(masterdir+"24.mp3.temp", masterdir+"24.mp3")
