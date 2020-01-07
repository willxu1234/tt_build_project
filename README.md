tt_build_project
================
Includes all the software for the Theta Tau build project

Software team:
Will Xu 
Esther Zhao 
Neha Pusarla 
Rick Huynh 
Kyle Gillaspy 
Heather Gan 
Britney Tran 

## How to use:
The script will run automatically upon startup of the Raspberry pi. To stop, run:

`ps aux | grep python`

This will pipe all the processes running in the background to grep, and search
for all the ones that include python. Find the process number by finding the led.py
process, and it will be the leftmost number.

To kill the process, run:

`kill -kill [process number]`

if that fails, run

`kill -9 [process number]`


## Links
[https://tutorials-raspberrypi.com/how-to-control-a-raspberry-pi-ws2801-rgb-led-strip/]

## Directories (update as you add things)
led: contains all the LED software

## Initial configurations
`pip install Adafruit-WS2801`
`pip install Adafruit_GPIO`

1. Enable SPI using `sudo raspi-config`

`python ws2801_example.py`

To enable script on startup:
1. `crontab -e`
2. At the bottom, add the line:
   `@reboot python /home/pi/path/to/ur/script &`
3. This also means you can add whatever scripts you want at startup to this crontab.


## Making Changes
To make a change, first create a branch with `git checkout -b [branch name]`,
do your normal Git workflow, and
then push with `git push origin [branch name]`
then make a pull request and Will will approve it.

# Creating Sprites
1. Create a draw function in led/draw_led.py
2. Each character will be represented as a 10 x 8 rectangle contained in front at index start.
3. By convention, we typically want a one pixel border on each side of the character, two pixels on top, and one pixel on the bottom. This rule should only be ignored if creating multi-character sprites.
4. Create a case in led/led.py in the `draw_message` function. Be sure to pick a uniquely encoded, singular character.

## Current Letters
+ is theta
= is tau
<> is a rose with the stem to the left
() is a rose with the stem to the right
;:| is a hammer and tongs
o is a binary 0
l is a binary 1
e is epsilon
^ is delta

ac is plant
mg is DNA
ik is building
bd is rocket
fh is potion


We also have A-Z and 0-9, with . and ! as punctuation.
