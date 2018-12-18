import time
from copy import deepcopy
import RPi.GPIO as GPIO

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Number of LEDs.
PIXEL_COUNT = 160
PIXEL_ROW = 10
PIXEL_COL = 8

# Color constants.
DARK_RED = Adafruit_WS2801.RGB_to_color(128, 0, 0)
YELLOW = Adafruit_WS2801.RGB_to_color(255, 84, 3)

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
			draw_R(start * FULL_LETTER, message_color)
		elif letter == 'B':
			draw_B(start * FULL_LETTER, message_color)
		elif letter == 'D':
			draw_D(start * FULL_LETTER, message_color)
		elif letter == 'F':
			draw_F(start * FULL_LETTER, message_color)
		elif letter == 'I':
			draw_I(start * FULL_LETTER, message_color)
		elif letter == 'K':
			draw_K(start * FULL_LETTER, message_color)
		elif letter == 'A':
			draw_A(start * FULL_LETTER, message_color)
		elif letter == 'C':
			draw_C(start * FULL_LETTER, message_color)
		elif letter == 'E':
			draw_E(start * FULL_LETTER, message_color)
		elif letter == 'U':
			draw_U(start * FULL_LETTER, message_color)
		elif letter == 'S':
			draw_S(start * FULL_LETTER, message_color)
		elif letter == 'H':
			draw_H(start * FULL_LETTER, message_color)
		elif letter == '0':
			draw_zero(start * FULL_LETTER, message_color)
		elif letter == '1':
			draw_one(start * FULL_LETTER, message_color)
		elif letter == '2':
			draw_two(start * FULL_LETTER, message_color)
		elif letter == '3':
			draw_three(start * FULL_LETTER, message_color)
		elif letter == '4':
			draw_four(start * FULL_LETTER, message_color)
		elif letter == '5':
			draw_five(start * FULL_LETTER, message_color)
		elif letter == '6':
			draw_six(start * FULL_LETTER, message_color)
		elif letter == '7':
			draw_seven(start * FULL_LETTER, message_color)
		elif letter == '8':
			draw_eight(start * FULL_LETTER, message_color)
		elif letter == '9':
			draw_nine(start * FULL_LETTER, message_color)
		elif letter == '!':
			draw_exclamation(start * FULL_LETTER, message_color)
		elif letter == '.':
			draw_period(start * FULL_LETTER, message_color)
		elif letter == '+':
			draw_theta(start * FULL_LETTER, message_color)
		elif letter == '=':
			draw_tau(start * FULL_LETTER, message_color)
		elif letter == 'M':
			draw_M(start * FULL_LETTER, message_color)
		elif letter == 'O':
			draw_O(start * FULL_LETTER, message_color)
		elif letter == 'V':
			draw_V(start * FULL_LETTER, message_color)
		elif letter == 'Z':
			draw_Z(start * FULL_LETTER, message_color)
		elif letter == ' ':
			# Draw a full space.
			pass
		else:
			print("Unable to draw that letter.")
			pass

	#TODO: Create a loop that shifts everything over.
	draw_scrolling(pixels, wait)

# Assumes that the height is 7 and width of each letter is 5. Adds the word to the matrix at start.
def draw_R(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	front[2][start + 2] = color
	front[5][start + 2] = color

	front[2][start + 3] = color
	front[5][start + 3] = color
	front[6][start + 3] = color

	front[2][start + 4] = color
	front[5][start + 4] = color
	front[7][start + 4] = color

	for row in range(2, 6):
		front[row][start + 5] = color
	front[8][start + 5] = color

def draw_U(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[8][col] = color

def draw_S(start, color):
	for row in range(2, 6):
		front[row][start + 1] = color
	front[8][start + 1] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(6, 9):
		front[row][start + 5] = color

def draw_H(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[5][col] = color

def draw_A(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color
		front[5][col] = color

def draw_B(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	for num in range(2, 5):
		front[2][start + num] = color
		front[5][start + num] = color
		front[8][start + num] = color
	front[3][start + 5] = color
	front[4][start + 5] = color
	front[6][start + 5] = color
	front[7][start + 5] = color

def draw_D(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	for num in range(2,5):
		front[2][start + num] = color
		front[8][start + num] = color
	for row in range(3,8):
		front[row][start + 5] = color

def draw_F(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	for num in range(2,5):
		front[2][start + num] = color
		front[5][start + num] = color

def draw_I(start, color):
	for row in range(3,8):
		front[row][start + 3] = color
	for num in range(1,6):
		front[2][start + num] = color
		front[8][start + num] = color

def draw_K(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
	front[5][start + 2] = color
	front[4][start + 3] = color
	front[3][start + 4] = color
	front[2][start + 5] = color
	front[6][start + 3] = color
	front[7][start + 4] = color
	front[8][start + 5] = color

def draw_M(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
		front[row][start + 5] = color
	front[3][start + 2] = color
	front[4][start + 3] = color
	front[3][start + 4] = color

def draw_O(start, color):
	for row in range(2,9):
		front[row][start + 1] = color
		front[row][start + 5] = color
	for num in range(2,5):
		front[2][start + num] = color
		front[8][start + num] = color

def draw_V(start, color):
	for row in range(2,6):
		front[row][start + 1] = color
		front[row][start + 5] = color
	front[7][start + 2] = color
	front[8][start + 3] = color
	front[7][start + 4] = color

def draw_Z(start, color):
	for num in range(1,6):
		front[2][start + num] = color
		front[8][start + num] = color
	front[3][start + 5] = color
	front[4][start + 5] = color
	front[5][start + 4] = color
	front[6][start + 3] = color
	front[7][start + 2] = color
	front[8][start + 5] = color

def draw_C(start, color):
	for row in range(2, 9):
		front[row][start+1] = color

	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[8][col] = color

def draw_E(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

def draw_G(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
	for row in range(5, 9):
		front[row][start + 5] = color
	for col in range(2, 6):
		front[2][col] = color
		front[8][col] = color
	for col in range(3, 6):
		front[5][col] = color

def draw_Y(start,color):
	for row in range(5, 9):
		front[row][start + 3] = color

	front[4][start + 4] = color
	front[4][start + 6] = color
	front[3][start + 3] = color
	front[3][start + 7] = color
	front[2][start + 2] = color
	front[2][start + 8] = color

def draw_W(start,color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	front[6][start + 2] = color
	front[6][start + 4] = color
	front[5][start + 3] = color

def draw_T(start, color):
	for row in range(2, 9):
		front[row][start + 3] = color

	for col in range(start + 1, start + 6):
		front[2][col] = color

	for row in range(6, 9):
		front[row][start + 5] = color

def draw_P(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color
		front[6][col] = color

	for row in range(3, 6):
		front[row][start + 5] = color

def draw_N(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	front[4][start + 2] = color
	front[5][start + 3] = color
	front[6][start + 4] = color

def draw_L(start, color):
	for row in range(2, 9):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[8][col] = color

def draw_X(start, color):
	for row in range(2, 4):
		front[row][start + 1] = color
		front[row][start + 5] = color

	for row in range(7, 9):
		front[row][start + 1] = color
		front[row][start + 5] = color

	front[4][start + 2] = color
	front[6][start + 2] = color
	front[4][start + 4] = color
	front[6][start + 4] = color
	front[5][start + 3] = color

def draw_Q(start, color):
	for row in range(3, 8):
		front[row][start + 1] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color

	for row in range(3, 7):
		front[row][start + 5] = color

	front[8][start + 2] = color
	front[8][start + 3] = color
	front[6][start + 3] = color
	front[7][start + 4] = color
	front[8][start + 5] = color

def draw_J(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color

	for row in range(3, 9):
		front[row][start + 3] = color

	front[8][start + 2] = color
	front[8][start + 1] = color
	front[7][start + 1] = color
	front[6][start + 1] = color
def draw_exclamation(start, color):
	for row in range(2, 7):
		front[row][start + 1] = color
	front[8][start + 1] = color

def draw_period(start, color):
	front[8][start + 1] = color

def draw_zero(start, color):
	for row in range(3, 8):
		 front[row][start + 1] = color
		 front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[2][col] = color
		front[8][col] = color

	front[6][start + 2] = color
	front[5][start + 3] = color
	front[4][start + 4] = color

def draw_one(start, color):
	front[3][start + 2] = color
	for row in range(2, 8):
		front[row][start + 3] = color

	for col in range(start + 2, start + 5):
		front[8][col] = color

def draw_two(start, color):
	for row in range(2, 6):
		front[row][start + 5] = color
	front[8][start + 5] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(6, 9):
		front[row][start + 1] = color

def draw_three(start, color):
	for row in range(2, 9):
		front[row][start + 5] = color

	for col in range(start + 2, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

def draw_four(start, color):
	for row in range(2, 6):
		front[row][start + 1] = color

	for row in range(2, 9):
		front[row][start + 5] = color

	for col in range(start + 2, start + 5):
		front[5][col] = color

def draw_five(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color

	for row in range(3, 6):
		front[row][start + 1] = color

	for col in range(start + 2, start + 6):
		front[5][col] = color

	for col in range(start + 2, start + 5):
		front[8][col] = color
	front[7][start + 1] = color

	for row in range(5, 8):
		front[row][start + 5] = color

def draw_six(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 8):
		front[row][start + 1] = color

	for row in range(6, 8):
		front[row][start + 5] = color

def draw_seven(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color

	front[8][start + 1] = color
	front[7][start + 1] = color
	front[6][start + 2] = color
	front[5][start + 3] = color
	front[4][start + 4] = color
	front[3][start + 5] = color

def draw_eight(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 8):
		front[row][start + 1] = color
		front[row][start + 5] = color

def draw_nine(start, color):
	for col in range(start + 1, start + 6):
		front[2][col] = color
		front[5][col] = color
		front[8][col] = color

	for row in range(2, 6):
		front[row][start + 1] = color

	for row in range(2, 8):
		front[row][start + 5] = color

def draw_theta(start, color):
        # column 1
        ar = [2,6]
        for row in range(3, 8):
            for i in range(len(ar)):
                front[row][start + ar[i]] = color

        ar_row = [2,5,8]
        # column 3 to 4
	for i in range(len(ar_row)):
            for col in range(3,6):
                front[ar_row[i]][start + col] = color


def draw_tau(start, color):
        for col in range(2,7):
            front[2][start + col] = color
        for row in range(3,9):
            front[row][start + 4] = color
        # serif details
        front[3][start + 2] = color
        front[3][start + 6] = color

        front[8][start + 3] = color
        front[8][start + 5] = color

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
		draw_message(pixels, 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+=', DARK_RED, YELLOW, 0.06)
