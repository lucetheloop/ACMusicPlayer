# ACMusicPlayer

Program that allows you to play animal crossing hourly music in real time, from a game in the series of your choice.

## Setup

1. Clone the repo
2. Insert music files for every game you wish to listen to into the relevant subdirectory of /Music.
3. Run format.py on every subdirectory you put files into (see Usage below)

## Usage

### format.py

This is used to rename files to a format readable by the program. It does *NOT* back up the files, so you should do this yourself.

``python format.py [directory]`` will format the files in the directory.

**NOTE**: Every file should already have "XX(AM/PM)" in the title for the tool to work, for instance "Animal Crossing 12AM" and "4PM City Folk" are valid titles to be formatted, "Wild World 9" and "New Leaf Hourly Music" are not.

### play.py

This is the main program, that plays music hourly, changing with real time.

``python format.py [-pg|-ww|-cf|-nl|-nh|--volume=VOLUME]``

#### Options:

 - ``-pg`` Play music from *Population Growing*
 - ``-ww`` Play music from *Wild World*
 - ``-cf`` Play music from *City Folk*
 - ``-nl`` Play music from *New Leaf*
 - ``-nh`` Play music from *New Horizons*

 - ``--vol`` Float between 0 and 1. Sets volume of music.
