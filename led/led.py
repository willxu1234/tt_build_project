import time
import socket
import subprocess
import random
import draw_led
from led_colors import *
from copy import deepcopy
import RPi.GPIO as GPIO

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Number of LEDs.
PIXEL_COUNT = 160
PIXEL_ROW = 10
PIXEL_COL = 8

# Dimensions of a letter.
LETTER_HEIGHT = 7
LETTER_WIDTH = 5
TOP_MARGIN = 2
BOT_MARGIN = 1
SPACE = 1
FULL_LETTER = 2 * SPACE + LETTER_WIDTH

# Contains all the pixel values. Sets all values to red by default.
# back contains every other column of 10.
front = [[] for r in range(PIXEL_ROW)]
for row in front:
	for c in range(PIXEL_COL):
		row.append(Adafruit_WS2801.RGB_to_color(128, 0, 0))

back = deepcopy(front)

# Decides the hue of the back. Goes from 0 to 255.
pos = 0

#for row in matrix:
#	for col in row:
#		print str(col) + ' '
#	print "\n"

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE), gpio=GPIO)

# Returns the index of the pixel given a row and column value. Set back to
# true if querying the back index.
def mat_to_pixel(row, col, back):
	pix = -1
	if back:
		pix = col * 2 * PIXEL_ROW + row
	else:
		pix = col * 2 * PIXEL_ROW + 10 + (PIXEL_ROW - row - 1)
	if pix < 0 or pix >= PIXEL_COUNT:
		print("Pixel value " + str(pix) + " out of range!")
		return -1
	return pix

# Takes the values in front and back and draws it to the LEDs.
# start indicates the starting index of the sliding window used to draw front
def draw_matrices(pixels, start=0):
	# Contains the pixel index.
	pix = 0

	if start + PIXEL_COL > len(front[0]):
		print "Start index is out of bounds."
		return

	pixels.clear()
	for row in range(PIXEL_ROW):
		for col in range(PIXEL_COL):
			pixels.set_pixel(mat_to_pixel(row, col, True), back[row][col])
	for row in range(PIXEL_ROW):
		for col in range(start, PIXEL_COL + start):
			pixels.set_pixel(mat_to_pixel(row, col - start, False), front[row][col])
	pixels.show()

# Scrolls across all of front with time wait in between renders.
def draw_scrolling(pixels, rainbow=True, wait=0.5):
	for start in range(len(front[0]) - FULL_LETTER):
		# Paint the background if necessary.
		if rainbow:
			augment_hue()
		draw_matrices(pixels, start)
		time.sleep(wait)

# Paints the front of the matrix with the rainbow of the back.
# wait_between is the seconds between each rendering.
# duration is the total amount of the time for this display to be up.
def rainbow_front(pixels, wait_between=0.03, duration=5):
	global front
	it = int(duration // wait_between)
	for i in range(it):
		# Make the back the next color
		augment_hue()
		draw_matrices(pixels, 0)
		time.sleep(wait_between)

# Static display of Theta Tau letters
def draw_letters(pixels, color, background_color, wait=0.5):
		global front
		del front[:]
		# Use up entire front space
		front = [[] for r in range(PIXEL_ROW)]
		for row in front:
			for c in range( PIXEL_COL ):
				row.append( background_color )
		draw_theta(0, color)
		draw_matrices(pixels, 0)
		time.sleep(wait)
		del front[:]
		front = [[] for r in range(PIXEL_ROW)]
		for row in front:
			for c in range( PIXEL_COL ):
				row.append( background_color )
		draw_tau(0, color)
		draw_matrices(pixels, 0)
		time.sleep(wait)

# Draws the message in message_color with a background color. rainbow decides whether or not the back
# will be sweep through the rainbow colors.
def draw_message(pixels, message, message_color, background_color, rainbow=True, wait=0.5):
	message_col_count = FULL_LETTER * len(message)
	global front
	if PIXEL_COL < message_col_count:
		del front[:]
		# Reallocate front so it fits the new matrix size.
		front = [[] for r in range(PIXEL_ROW)]
		for row in front:
			for c in range(message_col_count + 2 * PIXEL_COL):
				row.append(background_color)

	for start in range(1, len(message) + 1):
		letter = message[start - 1]
		if letter == 'R':
			draw_led.draw_R(start * FULL_LETTER, message_color, front)
		elif letter == 'B':
			draw_led.draw_B(start * FULL_LETTER, message_color, front)
		elif letter == 'D':
			draw_led.draw_D(start * FULL_LETTER, message_color, front)
		elif letter == 'F':
			draw_led.draw_F(start * FULL_LETTER, message_color, front)
		elif letter == 'I':
			draw_led.draw_I(start * FULL_LETTER, message_color, front)
		elif letter == 'K':
			draw_led.draw_K(start * FULL_LETTER, message_color, front)
		elif letter == 'A':
			draw_led.draw_A(start * FULL_LETTER, message_color, front)
		elif letter == 'C':
			draw_led.draw_C(start * FULL_LETTER, message_color, front)
		elif letter == 'E':
			draw_led.draw_E(start * FULL_LETTER, message_color, front)
		elif letter == 'e':
			draw_led.draw_epsilon(start * FULL_LETTER, message_color, front)
		elif letter == 'U':
			draw_led.draw_U(start * FULL_LETTER, message_color, front)
		elif letter == 'S':
			draw_led.draw_S(start * FULL_LETTER, message_color, front)
		elif letter == 'H':
			draw_led.draw_H(start * FULL_LETTER, message_color, front)
		elif letter == '0':
			draw_led.draw_zero(start * FULL_LETTER, message_color, front)
		elif letter == '1':
			draw_led.draw_one(start * FULL_LETTER, message_color, front)
		elif letter == '2':
			draw_led.draw_two(start * FULL_LETTER, message_color, front)
		elif letter == '3':
			draw_led.draw_three(start * FULL_LETTER, message_color, front)
		elif letter == '4':
			draw_led.draw_four(start * FULL_LETTER, message_color, front)
		elif letter == '5':
			draw_led.draw_five(start * FULL_LETTER, message_color, front)
		elif letter == '6':
			draw_led.draw_six(start * FULL_LETTER, message_color, front)
		elif letter == '7':
			draw_led.draw_seven(start * FULL_LETTER, message_color, front)
		elif letter == '8':
			draw_led.draw_eight(start * FULL_LETTER, message_color, front)
		elif letter == '9':
			draw_led.draw_nine(start * FULL_LETTER, message_color, front)
		elif letter == '!':
			draw_led.draw_exclamation(start * FULL_LETTER, message_color, front)
		elif letter == '.':
			draw_led.draw_period(start * FULL_LETTER, message_color, front)
		elif letter == '+':
			draw_led.draw_theta(start * FULL_LETTER, message_color, front)
		elif letter == '=':
			draw_led.draw_tau(start * FULL_LETTER, message_color, front)
		elif letter == '^':
			draw_led.draw_delta(start * FULL_LETTER, message_color, front)
		elif letter == 'M':
			draw_led.draw_M(start * FULL_LETTER, message_color, front)
		elif letter == 'O':
			draw_led.draw_O(start * FULL_LETTER, message_color, front)
		elif letter == 'V':
			draw_led.draw_V(start * FULL_LETTER, message_color, front)
		elif letter == 'Z':
			draw_led.draw_Z(start * FULL_LETTER, message_color, front)
		elif letter == 'G':
			draw_led.draw_G(start * FULL_LETTER, message_color, front)
		elif letter == 'J':
			draw_led.draw_J(start * FULL_LETTER, message_color, front)
		elif letter == 'L':
			draw_led.draw_L(start * FULL_LETTER, message_color, front)
		elif letter == 'N':
			draw_led.draw_N(start * FULL_LETTER, message_color, front)
		elif letter == 'P':
			draw_led.draw_P(start * FULL_LETTER, message_color, front)
		elif letter == 'T':
			draw_led.draw_T(start * FULL_LETTER, message_color, front)
		elif letter == 'W':
			draw_led.draw_W(start * FULL_LETTER, message_color, front)
		elif letter == 'Y':
			draw_led.draw_Y(start * FULL_LETTER, message_color, front)
		elif letter == 'Q':
			draw_led.draw_Q(start * FULL_LETTER, message_color, front)
		elif letter == 'X':
			draw_led.draw_X(start * FULL_LETTER, message_color, front)
		elif letter == '<':
			draw_led.draw_rose_left(start * FULL_LETTER, front)
		elif letter == '>':
			draw_led.draw_rose_right(start * FULL_LETTER, front)
		elif letter == '(':
			draw_led.draw_reverse_rose_left(start * FULL_LETTER, front)
		elif letter == ')':
			draw_led.draw_reverse_rose_right(start * FULL_LETTER, front)
		elif letter == ';':
			draw_led.draw_ht_left(start * FULL_LETTER, front)
		elif letter == ':':
			draw_led.draw_ht_mid(start * FULL_LETTER, front)
		elif letter == '|':
			draw_led.draw_ht_right(start * FULL_LETTER, front)
		elif letter == 'a':
			draw_led.draw_plant_left(start * FULL_LETTER, front)
		elif letter == 'c':
			draw_led.draw_plant_right(start * FULL_LETTER, front)
		elif letter == 'm':
			draw_led.draw_dna_left(start * FULL_LETTER, front)
		elif letter == 'g':
			draw_led.draw_dna_right(start * FULL_LETTER, front)
		elif letter == 'i':
			draw_led.draw_build_left(start * FULL_LETTER, front)
		elif letter == 'k':
			draw_led.draw_build_right(start * FULL_LETTER, front)
		elif letter == 'b':
			draw_led.draw_rocket(start * FULL_LETTER, front)
		elif letter == 'd':
			draw_led.draw_rocket2(start * FULL_LETTER, front)
		elif letter == 'f':
			draw_led.draw_potion(start * FULL_LETTER, front)
		elif letter == 'h':
			draw_led.draw_potion2(start * FULL_LETTER, front)
		elif letter == 'o':
			draw_led.draw_zero(start * FULL_LETTER, LIGHT_GREEN, front)
		elif letter == 'l':
			draw_led.draw_one(start * FULL_LETTER, LIGHT_GREEN, front)
		elif letter == ' ':
			# Draw a full space.
			pass
		else:
			print("Unable to draw that letter.")
			pass

	draw_scrolling(pixels, rainbow, wait)

# Sets the back color to the next hue in the rainbow.
def augment_hue():
	global front
	global pos

	hue = 0
	if pos < 85:
		hue = Adafruit_WS2801.RGB_to_color(pos * 3, 255 - pos, 0)
	elif pos < 170:
		hue = Adafruit_WS2801.RGB_to_color(255 - (pos - 85) * 3, 0, (pos - 85) * 3)
	else:
		hue = Adafruit_WS2801.RGB_to_color(0, (pos - 170) * 3, 255 - (pos - 170) * 3)

	for row in range(PIXEL_ROW):
		for col in range(PIXEL_COL):
			front[row][col] = hue

	pos = (pos + 1) % 255

# Sets the colors of one side of the wood panel to red and everything else to green.
def one_side(pixels):
	for i in range(pixels.count()):
		if i % 20 < 10:
			pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(255, 84, 3))
		else:
			pixels.set_pixel(i, Adafruit_WS2801.RGB_to_color(128, 0, 0))
	pixels.show()

if __name__ == "__main__":
	pixels.clear()
	draw_message(pixels, "WELCOME!", YELLOW, BLACK, True, 0.09)

	# Display a rainbow display on the front for 10 seconds.
	rainbow_front(pixels, wait_between=0.005, duration=10)
	
	no_ip = True

	while True:
		if no_ip:
			try:
				ip = subprocess.check_output(["hostname", "-I"]).split(' ')[0]
				socket.inet_aton(ip)
				no_ip = False
				draw_message(pixels, "IP FOUND. ", YELLOW, BLACK, True, 0.05)
				draw_message(pixels, ip, LIGHT_GREEN, BLACK, True, 0.2)
			except socket.error:
				# No ip address found yet
				pass
		value = random.randint(0,8)
		# += are reserved chars for Theta Tau symbols
		if value == 0:
			draw_message(pixels, '<>RUSH +=()', DARK_RED, BLACK, True, 0.09)
		elif value == 1:
			draw_message(pixels, 'e^', YELLOW, BLACK, True, 0.09)
			draw_message(pixels, 'CHAPTER', DARK_RED, BLACK, True, 0.09)
		elif value == 2:
 			draw_message(pixels, "NOW ACCEPTING MATH CS AND DATA SCIENCE!", WHITE, BLACK, True, 0.09)
		elif value == 3:
			# Display sprites
			draw_message(pixels, "ololacmgbdfh", DARK_RED, BLACK, True, 0.09)
		elif value == 4:
			draw_message(pixels, '<>();:|<>()', DARK_RED, BLACK, True, 0.09)
		elif value == 5:
			draw_message(pixels, 'PROFESSIONAL ENGINEERING FRATERNITY', YELLOW, BLACK, True, 0.09)
		elif value == 6:
			draw_message(pixels, 'COME CHECK US OUT AT RUSH!', DARK_RED, BLACK, True, 0.09)
		elif value == 7:
			draw_message(pixels, 'MEET THE BROTHERS!', YELLOW, BLACK, True, 0.09)
		elif value == 8:
			draw_message(pixels, 'BROTHERHOOD', YELLOW, BLACK, True, 0.09)
			draw_message(pixels, 'PHILANTHROPY', LIGHT_GREEN, BLACK, True, 0.09)
			draw_message(pixels, 'PROFESSIONALISM', LIGHT_RED, BLACK, True, 0.09)
