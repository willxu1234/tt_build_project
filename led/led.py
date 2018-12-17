import time
from copy import deepcopy
import RPi.GPIO as GPIO

import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI

# Number of LEDs.
PIXEL_COUNT = 160
PIXEL_ROW = 10
PIXEL_COL = 8

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
def draw_matrices(pixels):
	# Contains the pixel index.
	pix = 0
	pixels.clear()
	for row in range(PIXEL_ROW):
		for col in range(PIXEL_COL):
			pixels.set_pixel(mat_to_pixel(row, col, True), back[row][col])
			pixels.set_pixel(mat_to_pixel(row, col, False), front[row][col])
	pixels.show()	


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
	time.sleep(3)
	front[8][4] = Adafruit_WS2801.RGB_to_color(0, 255, 0)
	back[8][4] = Adafruit_WS2801.RGB_to_color(0, 255, 0)
	draw_matrices(pixels)
