import time
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
def draw_scrolling(pixels, wait=0.5):
	for start in range(len(front[0]) - FULL_LETTER):
		draw_matrices(pixels, start)
		time.sleep(wait)

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

# Draws the message in message_color with a background color.
def draw_message(pixels, message, message_color, background_color, wait=0.5):
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
		elif letter == ' ':
			# Draw a full space.
			pass
		else:
			print("Unable to draw that letter.")
			pass

	#TODO: Create a loop that shifts everything over.
	draw_scrolling(pixels, wait)
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
	one_side(pixels)
	time.sleep(0.5)
	while True:
		# += are reserved chars for Theta Tau symbols
		# draw_message(pixels, '<>+=;:|e^()', DARK_RED, YELLOW, 0.06)
		draw_message(pixels, '<>+=;:|e^()', DARK_RED, Adafruit_WS2801.RGB_to_color(0, 0, 0), 0.06)
