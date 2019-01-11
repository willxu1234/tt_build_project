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
		front = deepcopy(back)
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
	# message_col_count = FULL_LETTER * len(message)
	message_col_count = 0
	for letter in message:
		# If the letter is in the hashmap defined in draw_led, make the front
		# matrix that much bigger. Otherwise, just assume the maximum letter
		# width.
		if letter in draw_led.LETTER_WIDTHS:
			message_col_count += draw_led.LETTER_WIDTHS[letter]
		else:
			message_col_count += FULL_LETTER
	global front
	if PIXEL_COL < message_col_count:
		del front[:]
		# Reallocate front so it fits the new matrix size.
		front = [[] for r in range(PIXEL_ROW)]
		for row in front:
			for c in range(message_col_count + 2 * PIXEL_COL):
				row.append(background_color)

	# index of the current letter
	index = 0
	while start < message_col_count:
		if letter == ' ':
			# Draw a full space.
			pass
		elif letter in draw_led.DRAW_FN:
			draw_led.DRAW_FN[letter](start, message_color, front)
		else:
			print("Unable to draw that letter.")
			pass

		index += 1
		if letter in draw_led.LETTER_WIDTHS:
			start += draw_led.LETTER_WIDTHS[letter]
		else:
			start += FULL_LETTER

	draw_scrolling(pixels, rainbow, wait)

# Sets the back color to the next hue in the rainbow.
def augment_hue():
	global back
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
			back[row][col] = hue

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
